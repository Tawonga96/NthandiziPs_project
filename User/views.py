import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from User.serializers import *
from rest_framework import generics, permissions
from django.contrib.auth.hashers import make_password
import secrets
from Community.models import Community, Member, Household, Citizen, Housemember, CommunityLeader
from django.core.mail import send_mail
import re

from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.core.mail import EmailMessage

from django.utils.crypto import get_random_string
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string


# Test views
class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            # check if email exist and phone no has 10digits
            # email = serializer.validated_data['email']
            # phone_number = serializer.validated_data['pnumber']

            # if User.objects.filter(email=email).exists():
            #     return Response({'message': 'Email already exists. Please use a different email.'}, status=status.HTTP_400_BAD_REQUEST)

            # if not re.match(r'^\d{10}$', phone_number):
            #     return Response({'message': 'Invalid phone number. Please provide a 10-digit phone number.'}, status=status.HTTP_400_BAD_REQUEST)

            # Perform registration logic here
            user = User.objects.create(
                fname=serializer.validated_data['fname'],
                lname=serializer.validated_data['lname'],
                pnumber=serializer.validated_data['pnumber'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],  
                otp=serializer.validated_data['otp'],
            ) 

            community = Community.objects.get(pk=request.data['community_id'])
            member = Member.objects.create(cid=user, community=community, date_joined=user.date_joined, citizen_typ='Citizen')
            household = Household.objects.create(date_added=user.date_joined, hh_name='New Household')
            housemember = Housemember.objects.create(mid=member, hhid=household, date_joined=user.date_joined)
            citizen = Citizen.objects.create(cid=user, occupation='Occupation')

            # Associate with community leader
            community_leader = CommunityLeader.objects.create(leader=member, community=community, elected_on=user.date_joined)

            # Generate token
            token = self.generate_token()
            # uid = urlsafe_base64_encode(user.pk.to_bytes())

            # Send confirmation email
            self.send_confirmation_email(user, token)
            
            # Return response
            return Response({'message': 'User registered successfully. Confirmation email sent.'}, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def generate_token(self):
        token = secrets.token_urlsafe(32)
        return token 


    def send_confirmation_email(self, user, token):
        subject = 'Nthandizi App Registration Confirmation'
        message = f'Hi {user.fname},\n\nThank you for registering with Nthandizi Police Service Application.\nYour account has been successfully created.\nYou can now Log in with the following details:\n\nFirstname: {user.fname}\n\nLastname: {user.lname}\n\nPhone No: {user.pnumber}\n\nEmail: {user.email}\n\nPassword: {user.password}\n\nOtp: {user.otp}\n\nPlease Remember to change the password after login the one is the default password'
        from_email = 'tawongachauluntha22@gmail.com'
        to_email = user.email 
        send_mail(subject, message, from_email, [to_email])



class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            fname = serializer.validated_data['fname']
            password = serializer.validated_data['password']
          
            try:
                # Perform login authentication
                user = User.objects.get(fname=fname, password=password)
                # Serialize the user data
                serializer = UserSerializer(user)  

                # Retrieve additional user data
                user_data = {
                    'uid': user.uid,
                    'fname': user.fname,
                    'lname': user.lname,
                    'password': user.password,
                    'email': user.email,
                    'pnumber': user.pnumber,
                }
                    # Serialize the user data
                    # serializer = UserSerializer(user)
                    # user_data.update(serializer.data)

                # Authentication successful
                return Response({'user_data': user_data}, status=status.HTTP_200_OK)

            except User.DoesNotExist:
                # Authentication failed
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class CommunityLeaderLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            fname = serializer.validated_data['fname']
            password = serializer.validated_data['password']
          
            try:
                # Perform login authentication for community leader
                user = User.objects.get(fname=fname, password=password, is_community_leader=True)
                # Serialize the user data
                serializer = UserSerializer(user)  

                # Retrieve additional user data
                user_data = {
                    'uid': user.uid,
                    'fname': user.fname,
                    'lname': user.lname,
                    'password': user.password,
                    'email': user.email,
                    'pnumber': user.pnumber,
                }
                
                # Authentication successful
                return Response({'user_data': user_data}, status=status.HTTP_200_OK)

            except User.DoesNotExist:
                # Authentication failed
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



















