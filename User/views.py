import random
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import hashlib
from django.http import JsonResponse

import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from User.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from User.serializers import UserSerializer
from User.serializers import LoginSerializer
from Community.models import *
from rest_framework.response import Response
from User.models import User
from twilio.rest import Client



class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegistration(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Generate a random 6-digit OTP
        otp = random.randint(1000, 9999)

        # Set the OTP and is_active in the validated data
        serializer.validated_data['otp'] = otp
        serializer.validated_data['is_active'] = 1  # Set is_active to 1

        # Extract validated data from the serializer
        fname = serializer.validated_data['fname']
        lname = serializer.validated_data['lname']
        pnumber = serializer.validated_data['pnumber']
        password = serializer.validated_data['password']
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        is_active = serializer.validated_data['is_active']

        # Hash the password before saving it to the database
        # hashed_password = hashlib.sha256(password.encode()).hexdigest()
      
        # Check if any of the required fields are empty
        if not fname or not lname or not pnumber or not password or not email:
            return Response({'error': 'Please provide values for all required fields.'},
                            status=status.HTTP_400_BAD_REQUEST)
       
        # Validate fname and lname format using custom validators
        fname = serializer.validated_data['fname']
        lname = serializer.validated_data['lname']
        if not self.validate_name(fname):
            return Response({'error': 'First name must start with an uppercase letter.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not self.validate_name(lname):
            return Response({'error': 'Last name must start with an uppercase letter.'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate the phone number format using a custom method
        pnumber = serializer.validated_data['pnumber']
        if not self.validate_phone_number(pnumber):
            return Response({'error': 'Phone number must have 13 digits and start with +265.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validate_email(email)
        except ValidationError:
            return Response({'error': 'Invalid email format.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the email already exists in the database
        # if User.objects.filter(email=email).exists():
        #     return Response({'error': 'Email already exists. Please use a different email.'}, status=status.HTTP_409_CONFLICT)

        # Validate the password format using custom password validator
        password = serializer.validated_data['password']
        if not self.validate_password(password):
            return Response({'error': 'Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user object
        user = User.objects.create(
            fname=fname,
            lname=lname,
            pnumber=pnumber,
            password=password,
            email=email,
            otp=otp,
            is_active=is_active,
        )

        # Send the confirmation email to the user
        self.send_confirmation_email(user)

        # Return a response with the created user data
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

    def send_confirmation_email(self, user):
        subject = 'Nthandizi App Registration Confirmation'
        message = f'''
        Hi {user.fname},

        Thank you for registering with Nthandizi Police Service Application.
        Your account has been successfully created.

        You can now Log in with the following details:

        UserID: {user.uid}
        Firstname: {user.fname}
        Lastname: {user.lname}
        Phone No: {user.pnumber}
        Email: {user.email}
        OTP: {user.otp}
        Date Joined: {user.date_joined.strftime("%Y-%m-%d %H:%M:%S")}

        Please Remember to change the password after login; the default password is provided for initial access.

        Regards,
        Nthandizi Police Service Application Team
        '''
        from_email = 'tawongachauluntha22@gmail.com'
        to_email = user.email 
        send_mail(subject, message, from_email, [to_email])

    def validate_password(self, password):
        # Validate password using regular expressions
        # Minimum 8 characters, at least one uppercase letter, one lowercase letter, and one digit
        password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
        return re.match(password_pattern, password)
    
    def validate_name(self, name):
        # Validate name to start with uppercase letter
        if not name[0].isupper():
            return False
        return True
    
    def validate_phone_number(self, pnumber):
       # Validate phone number to start with '+265' and have 13 digits in total
        return re.match(r'^\+265\d{9}$', pnumber)
    
class UserLogin(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            fname = request.data.get('fname')
            password = request.data.get('password')

            # Validate the request data
            if not fname or not password:
                return Response({'error': 'Please provide both fname and password.'}, status=status.HTTP_400_BAD_REQUEST)

            # Hash the provided password
            # hashed_password = hashlib.sha256(password.encode()).hexdigest()

            try:
                # Check if the user exists and the password matches
                user = User.objects.get(fname=fname, password=password)

                # Serialize the user data
                serializer = UserSerializer(user)
                user_data = serializer.data

                # Return the user data without the password
                user_data.pop('password', None)

                return Response({'user_data': user_data}, status=status.HTTP_200_OK)

            except User.DoesNotExist:
                # Authentication failed
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   



















































#     # def send_confirmation_email(self, user):
#     #     subject = 'Nthandizi App Registration Confirmation'
#     #     message = f'Hi {user.fname},\n\nThank you for registering with Nthandizi Police Service Application.\nYour account has been successfully created.\nYou can now Log in with the following details:\n\nFirstname: {user.fname}\n\nLastname: {user.lname}\n\nPhone No: {user.pnumber}\n\nEmail: {user.email}\n\nPassword: {user.password}\n\nOtp: {user.otp}\n\nPlease Remember to change the password after login the one is the default password'
#     #     from_email = 'tawongachauluntha22@gmail.com'
#     #     to_email = user.email 
#     #     send_mail(subject, message, from_email, [to_email])
#     def send_confirmation_sms(self, user):
#         account_sid = 'ACd8a3bc1036a690fdc8e2ff279906294c'
#         auth_token = '6241b58649c185f6300dde770aff394b'
#         twilio_phone_number = '+13609972230'

#         client = Client(account_sid, auth_token)

#         message = client.messages.create(
#             body=f'''
#             Hi {user.fname},

#             Thank you for registering with Nthandizi Police Service Application.
#             Your account has been successfully created.

#             You can now Log in with the following details:

#             User ID: {user.uid}
#             Firstname: {user.fname}
#             Lastname: {user.lname}
#             Phone No: {user.pnumber}
#             Email: {user.email}
#             OTP: {user.otp}
#             Date Joined: {user.date_joined.strftime("%Y-%m-%d %H:%M:%S")}

#             Please Remember to change the password after login; the default password is provided for initial access.

#             Regards,
#             Nthandizi Police Service Application Team
#             ''',
#             from_=twilio_phone_number,
#             to=user.pnumber  # Use the user's phone number for SMS
#         )