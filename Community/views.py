import re
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from Community.models import Citizen
from Community.serializers import *
from rest_framework import generics,permissions, status
from Community.models import Community, Member
from django.contrib.auth import authenticate
from User.models import User
from User.serializers import UserSerializer
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token
import random




class CommunityDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CommunityList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer 

class CommunityCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract validated data from the serializer
        district = serializer.validated_data['district']
        comm_name = serializer.validated_data['comm_name']
        area = serializer.validated_data.get('area')

        # Perform any additional validation or logic here before creating the community
        # Check if district and comm_name are provided and not empty
        if not district or not comm_name:
            return Response({"error": "Please provide both 'district' and 'comm_name' values."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check if district, comm_name, and area already exist as a combination
        community_exists = Community.objects.filter(district=district, comm_name=comm_name, area=area).exists()
        if community_exists:
            return Response({"error": "Community with the provided combination of 'district', 'comm_name', and 'area' already exists."},
                            status=status.HTTP_409_CONFLICT)

        # Create the Community object
        community = Community.objects.create(
            district=district,
            comm_name=comm_name,
            area=area,
        )

        # Return a response with the created community data
        return Response(CommunitySerializer(community).data, status=status.HTTP_201_CREATED)







class CitizenDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = CitizenSerializer

class CitizenList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = CitizenSerializer
    
class CitizenRegistration(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CitizenSerializer

    def create(self, request, *args, **kwargs):
        # Extract data from the request
        cid = request.data.get('cid')
        occupation = request.data.get('occupation')

        # # Validate the format of cid (6-character alphanumeric)
        if not re.match(r'^[a-zA-Z0-9]{6}$', cid):
            return Response({"error": "Please provide a valid 'citizen ID' (6-character alphanumeric)."}, status=status.HTTP_400_BAD_REQUEST)


         # Check if cid and occupation are provided and not empty
        if not cid or not occupation:
            return Response({"error": "Please provide both 'citizen ID' and 'occupation' values."}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the User object by User ID
        try:
            # #user = User.objects.get(pk=cid)
            # user = User.objects.get(uid=cid)
            user = User.objects.get(uid=str(cid))  # Convert cid to string for lookup


        except User.DoesNotExist:
            return Response({"error": "User with the provided ID does not exist."}, status=status.HTTP_400_BAD_REQUEST)


        # Check if a Citizen with the provided User (cid) already exists

        existing_citizen = Citizen.objects.filter(user=user).first()
        # existing_citizen = Citizen.objects.filter(cid__uid=cid).first()

        if existing_citizen:
            # If Citizen already exists, return a response indicating that the user is already registered as a Citizen
            return Response({"error": "User with the provided ID is already registered as a Citizen."},
                            status=status.HTTP_400_BAD_REQUEST)
        
        # Create the Citizen object with the provided User and occupation
        citizen = Citizen.objects.create(cid=cid, occupation=occupation ,user=user)

        # citizen = Citizen.objects.get(pk=cid)
        # Get the primary key of the created Citizen object
        # citizen_pk = citizen.pk

        # Send the confirmation email
        self.send_confirmation_email_citizen(user,citizen)

        # Return a response with the created citizen data
        return Response(CitizenSerializer(citizen).data, status=status.HTTP_201_CREATED)
    
    def send_confirmation_email_citizen(self, user, citizen):
        subject = 'Nthandizi App Registration Confirmation'
        message = f'''
        Hi {user.fname},

        Thank you for registering with Nthandizi Police Service Application.
        Your account has been successfully created.

        User ID: {user.uid}
        First Name: {user.fname}
        Last Name: {user.lname}
        Phone Number: {user.pnumber}
        Email: {user.email}
        Occupation: {citizen.occupation} 
        Date Joined {user.date_joined}

        We look forward to your active participation in making our community a safer place.

        Regards,
        Nthandizi Police Service Application Team
        '''
        from_email = 'tawongachauluntha22@gmail.com'
        to_email = user.email
        send_mail(subject, message, from_email, [to_email])
    
class CommunityLeaderDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = CommunityLeaderSerializer


class CommunityLeaderList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = CommunityLeaderSerializer

class CommunityLeaderCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = CommunityLeader.objects.all()
    serializer_class = CommunityLeaderSerializer

    def create(self, request, *args, **kwargs):
        # Extract the data from the request
        leader_id_pk = request.data.get('leader_id')
        community_id_pk = request.data.get('community_id')
        elected_on = request.data.get('elected_on')

        # Check if leader_id and community_id are provided and not empty
        if not leader_id_pk or not community_id_pk:
            return Response({'error': 'Please provide both "leader_id" and "community_id" values.'},
                            status=status.HTTP_400_BAD_REQUEST)
        
        # Check if a CommunityLeader with the provided leader_id and community_id already exists
        existing_leader = CommunityLeader.objects.filter(leader_id=leader_id_pk, community_id=community_id_pk).first()
        if existing_leader:
            return Response({'error': 'A CommunityLeader with the provided "leader_id" and "community_id" already exists.'},
                            status=status.HTTP_409_CONFLICT)


        # Get the Member instance for the selected leader
        try:
            leader_member = Member.objects.get(pk=leader_id_pk)
        except Member.DoesNotExist:
            return Response({'error': 'Member with the provided primary key does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Get the Community instance based on the community_id_pk
        try:
            community_instance = Community.objects.get(pk=community_id_pk)
        except Community.DoesNotExist:
            return Response({'error': 'Community with the provided primary key does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Perform any additional validation or logic here before creating the CommunityLeader

        # Create the CommunityLeader object using the selected leader and community
        community_leader = CommunityLeader.objects.create(
            leader_id=leader_id_pk,
            community_id=community_id_pk,
            elected_on=elected_on
        )

        # Return a response with the created CommunityLeader data
        return Response(CommunityLeaderSerializer(community_leader).data, status=status.HTTP_201_CREATED)




class HouseholdDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = HouseholdSerializer


class HouseholdList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = HouseholdSerializer

class HousememberDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = HousememberSerializer


class HousememberList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = HousememberSerializer





class MemberDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = MemberSerializer


class MemberList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = MemberSerializer

class MemberCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def create(self, request, *args, **kwargs):
        # Extract cid and community_id from the request data using get() method
        cid = request.data.get('cid')
        community_id_pk = request.data.get('community_id')
        citizen_typ = request.data.get('citizen_typ', 'Member')  # Retrieve citizen_typ from request data

        # Check if both cid and community_id are provided and not empty
        if not cid or not community_id_pk:
            return Response({'error': 'Please provide both "Citizen ID" and "Community ID" values.'},
                            status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the combination of cid and community_id already exists in the database
        existing_member = Member.objects.filter(cid=cid, community_id=community_id_pk).first()
        if existing_member:
            return Response({'error': 'A member with the provided "ID" and "community_id" already exists.'},
                            status=status.HTTP_409_CONFLICT)


        # Get the Citizen instance based on the provided cid
        try:
            # cid_instance = Citizen.objects.get(pk=cid_pk)
            cid_instance = Citizen.objects.get(cid=cid)

        except Citizen.DoesNotExist:
            return Response({'error': 'Citizen with the provided primary key does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Get the Community instance based on the provided community_id_pk
        try:
            community_instance = Community.objects.get(pk=community_id_pk)
        except Community.DoesNotExist:
            return Response({'error': 'Community with the provided primary key does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)


        # Create the Member object using the instances of Citizen and Community
        member = Member.objects.create(
            cid=cid_instance,
            community_id=community_instance.pk,
            citizen_typ=citizen_typ
        )
        # Return a response with the created member data
        return Response(MemberSerializer(member).data, status=status.HTTP_201_CREATED)
