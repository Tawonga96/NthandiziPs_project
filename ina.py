from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from User.serializers import *

from rest_framework import generics, permissions
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

from django.utils.http import urlsafe_base64_encode
import secrets
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
            # Perform registration logic here
            user = User.objects.create(
                fname=serializer.validated_data['fname'],
                lname=serializer.validated_data['lname'],
                pnumber=serializer.validated_data['pnumber'],
                email=serializer.validated_data['email'],
                password=make_password(serializer.validated_data['password']),  
                otp=serializer.validated_data['otp'],
            ) 
            # Generate token
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
        message = f'Hi {user.fname},\nThank you for registering with Nthandizi Police Service Application.\nYour account has been successfully created.\nYou can now Log in with the following details:\n\nFirstname: {user.fname}\n\nLastname: {user.lname}\n\nPhone No: {user.pnumber}\n\nEmail: {user.email}\n\n\nPassword: {user.password}\n\nOtp: {user.otp}\nPlease Remember to change the password after login the one is the default password'
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
                serializer = UserSerializer(user)  # Serialize the user data

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



























# Create your views here.
# class UserDetail(generics.RetrieveAPIView):
#     permission_classes = [permissions.AllowAny]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserList(generics.ListCreateAPIView):
#     permission_classes = [permissions.AllowAny]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


    # def post(self, request, *args, **kwargs):
    #     login_serializer = LoginSerializer(data=request.data.get('login'))
    #     if login_serializer.is_valid():
            # Perform login logic here
            # fname = login_serializer.validated_data['fname']
            # password = login_serializer.validated_data['password']
    
            # user = authenticate(username=fname, password=password)

            # if user is not None:
                # User is authenticated, perform login
                # login(request, user)
                # Generate tokens or manage sessions as required
                # return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            # else:
                # Invalid credentials
                # return Response({'message': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # serializer = self.get_serializer(data=request.data)
        # if serializer.is_valid():
            # Perform registration logic here
            # Get the validated data from the serializer
            # validated_data = serializer.validated_data

            # Generate a hashed password using Django's make_password function
            # hashed_password = make_password(validated_data['password'])

            # Create a 
            # new user instance with the validated data and hashed password
            # user = User(
            #     fname=validated_data['fname'],
            #     lname=validated_data['lname'],
            #     pnumber=validated_data['pnumber'],
            #     password=hashed_password,
            #     email=validated_data.get('email'),
            #     otp=validated_data.get('otp'),
            #     is_active=validated_data.get('is_active')
            # )

            # Save the user to the database
            # user.save()

            # You can perform any additional actions or validations here
    
            
        #     return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserList(generics.ListCreateAPIView):
#     permission_classes = [permissions.AllowAny]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class LoginView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             fname = serializer.validated_data['fname']
#             password = serializer.validated_data['password']
            # Perform login authentication
            # try:
                # Perform login authentication
                # user = User.objects.get(fname=fname, password=password)
                # serializer = UserSerializer(user)  # Serialize the user data
                # Authentication successful
                # return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            # except User.DoesNotExist:
                # Authentication failed
                # return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            
        # else:
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Detail(generics.RetrieveAPIView) 
#List(genereics.ListAPIView)


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
                serializer = UserSerializer(user)  # Serialize the user data

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



