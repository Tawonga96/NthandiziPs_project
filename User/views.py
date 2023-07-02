import datetime
# from Community.models import Citizen, Member, CommunityLeader, Household, Housemember

# from Community.models import Community, Member, Household, Citizen, Housemember, CommunityLeader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from User.serializers import *
from rest_framework import generics, permissions
# from django.contrib.auth.hashers import make_password
import secrets
from django.core.mail import send_mail
# import re
# from User.models import User, Citizen, Member, CommunityLeader, Household, Housemember
# from .serializers import UserSerializer

from Community.models import Citizen, Member, CommunityLeader, Household, Housemember
from User.models import User




# from django.contrib.auth import authenticate, login
# from rest_framework.authtoken.models import Token
# from django.core.mail import EmailMessage

# from django.utils.crypto import get_random_string
# from django.utils.http import urlsafe_base64_encode
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# from django.template.loader import render_to_string


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
            #extract data from validated serializer before creating the user object
            fname = serializer.validated_data['fname']
            lname = serializer.validated_data['lname']
            pnumber = serializer.validated_data['pnumber']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            otp = serializer.validated_data['otp']
            is_community_leader = serializer.validated_data.get('is_community_leader', False)
           
            # Perform registration logic here
            user = User.objects.create(
                fname=fname,
                lname=lname,
                pnumber=pnumber,
                email=email,
                password=password,
                otp=otp,
                is_community_leader=is_community_leader,
                is_active=1
            )
            # Save the user object before creating related objects
            user.save()
            # Associate with community leader
            if is_community_leader:
                community_leader = CommunityLeader.objects.create(leader=user)
                user.community_leader = community_leader
                # Assign the community ID based on the selected community in the serializer
                community = serializer.validated_data.get('community_leader').get('community')
                community_leader.community = community
                community_leader.save()
               

            # Save the user object
            user.save()

            token = self.generate_token()

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
                # Check if the credentials belong to a community leader
                user = User.objects.get(fname=fname, password=password)
                if not user.is_community_leader:
                    return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

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

















  # check if email exist and phone no has 10digits
            # email = serializer.validated_data['email']
            # phone_number = serializer.validated_data['pnumber']

            # if User.objects.filter(email=email).exists():
            #     return Response({'message': 'Email already exists. Please use a different email.'}, status=status.HTTP_400_BAD_REQUEST)

            # if not re.match(r'^\d{10}$', phone_number):
            #