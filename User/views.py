import random
import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from Cases.serializers import MemberSerializer
from Nthandizi_ps import settings
from PoliceStation.models import *
from User.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.views import APIView

from User.serializers import UserSerializer, LoginSerializer

from Community.models import *
# from Community.models import Member, Citizen  # Import the Member and Citizen models
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

# USER REGISTRATION 
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
        serializer.validated_data['is_active'] = False  # Set is_active to 1

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

        if not self.validate_name(fname):
            return Response({'message': 'First name must start with an uppercase letter.'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        # Validate the phone number format using a custom method
        pnumber = serializer.validated_data['pnumber']
        if not self.validate_phone_number(pnumber):
            return Response({'message': 'Phone number must have 13 digits and start with +265.'}, status=status.HTTP_411_LENGTH_REQUIRED)

        try:
            validate_email(email)
        except ValidationError:
            return Response({'message': 'Invalid email format.'}, status=status.HTTP_403_FORBIDDEN)

        # Check if the email already exists in the database
        # if User.objects.filter(email=email).exists():
        #     return Response({'error': 'Email already exists. Please use a different email.'}, status=status.HTTP_409_CONFLICT)

        # Validate the password format using custom password validator
        password = serializer.validated_data['password']
        if not self.validate_password(password):
            return Response({'message': 'Validate with minimum 6 characters, one number, one symbol.'}, status=status.HTTP_401_UNAUTHORIZED)

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

        ## Generate the uid for the user
        # uid = generate_random_uid()
        # user.uid = uid
        # user.save()

        # Send the confirmation email to the user
        # Twilio account
        # self.send_confirmation_sms(user)
        # Email account
        self.send_confirmation_email(user)

        # Return a response with the created user data
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

        
    def send_confirmation_sms(self, user):
        account_sid= settings.TWILIO_ACCOUNT_SID
        auth_token= settings.TWILIO_AUTH_TOKEN 
        twilio_phone =settings.TWILIO_PHONE_NUMBER

        client = Client(account_sid, auth_token)

        sms_message = f'''
        Hi {user.fname},

        Your User ID is: {user.uid}.

        Now, you can proceed with the registration and pass the ID to your community leader to add you to your community
        
        '''
        to_phone_number = user.pnumber

        client.messages.create(
            body=sms_message,
            from_=twilio_phone,
            to=to_phone_number
        )

    
    def send_confirmation_email(self, user):
        subject = 'Nthandizi App Registration Confirmation'
        message = f'''
        Hi {user.fname},

        Your User ID is: {user.uid}.

        Now, you can proceed with the registration and pass the UserID to your community leader to activate this account
        
        Regards,
        Nthandizi Police Service Application Team

        '''
        from_email = 'tawongachauluntha22@gmail.com'
        to_email = user.email 
        send_mail(subject, message, from_email, [to_email])


    def validate_password(self, password):
        # Validate password using regular expressions
        # Minimum 6 characters, one number, one symbol
        password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{6,}$"
        return re.match(password_pattern, password)
    
    def validate_name(self, name):
        # Validate name to start with uppercase letter
        if not name[0].isupper():
            return False
        return True
    
    def validate_phone_number(self, pnumber):
       # Validate phone number to start with '+265' and have 13 digits in total
        return re.match(r'^\+265\d{9}$', pnumber)











# USER / MEMBER LOGIN LOGIC
class UserLogin(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            fname = serializer.validated_data.get('fname')
            password = serializer.validated_data.get('password')

            try:
                user = User.objects.get(fname=fname)
            except User.DoesNotExist:
                return Response({'error': 'User with the provided First Name does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

            if user.password != password:
                return Response({'error': 'Invalid password.'}, status=status.HTTP_401_UNAUTHORIZED)

            # Check if the user is active
            if not user.is_active:
                return Response({'message': 'Your account is not yet activated.'}, status=status.HTTP_403_FORBIDDEN)

            user_data = UserSerializer(user)
            user_data.data.pop('password', None)

            return Response({'message': 'Authentication successful.', 'user_data': user_data.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    








# COMMUNITY LEADER LOGIN LOGIC
class CommunityLeaderLogin(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            fname = serializer.validated_data.get('fname')
            password = serializer.validated_data.get('password')

            try:
                user = User.objects.get(fname=fname)
            except User.DoesNotExist:
                return Response({'error': 'User with the provided First Name does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
    
            if user.password != password:
                return Response({'error': 'Invalid password.'}, status=status.HTTP_401_UNAUTHORIZED)

            # Check if the user is active
            if not user.is_active:
                return Response({'message': 'Your account is not yet activated.'}, status=status.HTTP_403_FORBIDDEN)

            # Check if the user is a community leader by retrieving the Member instance
            try:
                member = Member.objects.get(cid=user.citizen.cid)
            except Member.DoesNotExist:
                return Response({'error': 'User is not a community leader.'}, status=status.HTTP_403_FORBIDDEN)

            if member.citizen_typ != 'Leader':
                return Response({'error': 'User is not a community leader.'}, status=status.HTTP_403_FORBIDDEN)

            user_data = UserSerializer(user)
            user_data.data.pop('password', None)

            return Response({'message': 'Authentication successful.', 'user_data': user_data.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# POLICE OFFICER LOGIN LOGIC
class PoliceOfficerLogin(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            fname = serializer.validated_data.get('fname')
            password = serializer.validated_data.get('password')

            try:
                user = User.objects.get(fname=fname)
            except User.DoesNotExist:
                return Response({'error': 'User with the provided First Name does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the user is a police officer by retrieving the PoliceOfficer instance
            try:
                police_officer = Policeofficer.objects.get(pid=user.policeofficer.pid)
            except Policeofficer.DoesNotExist:
                return Response({'error': 'User is not a police officer.'}, status=status.HTTP_403_FORBIDDEN)

            # Check if the user's password matches
            if user.password != password:
                return Response({'error': 'Invalid password.'}, status=status.HTTP_401_UNAUTHORIZED)

            # Check if the user is active
            if not user.is_active:
                return Response({'message': 'Your account is not yet activated.'}, status=status.HTTP_403_FORBIDDEN)

            user_data = UserSerializer(user)
            user_data.data.pop('password', None)

            return Response({'message': 'Authentication successful.', 'user_data': user_data.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ACCOUNT ACTIVATION
class AccountActivation(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        # Extract uid from the request data using get() method
        uid = request.data.get('uid')

        # Check if uid is provided and not empty
        if not uid:
            return Response({'error': 'Please provide the UserID value.'}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the User object by uid
        try:
            user = User.objects.get(uid=uid)
        except User.DoesNotExist:
            return Response({'error': 'User with the provided UserID does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user account is already active
        if user.is_active:
            return Response({'message': 'User account is already activated.'}, status=status.HTTP_200_OK)

        # Activate the user account by setting is_active to True
        user.is_active = True
        user.save()

        # Serialize the user data
        user_serializer = UserSerializer(user)

        # Return a response with the user details and a success message
        return Response({'message': 'User account has been activated.', 'user': user_serializer.data}, status=status.HTTP_200_OK)






















































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