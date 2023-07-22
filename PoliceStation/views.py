from rest_framework import serializers
from Community.models import Community
from PoliceStation.serializers import *
from rest_framework import generics, permissions,status
from rest_framework.response import Response
from PoliceStation.models import Policeofficer
from PoliceStation.serializers import PoliceofficerSerializer

from User.models import User  # Import User model here

# Create your views here.
# Job posting
class JobPostingDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = JobPostingSerializer


class JobPostingList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = JobPostingSerializer


# police officer
class PoliceofficerDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = PoliceofficerSerializer


class PoliceofficerList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = PoliceofficerSerializer


class PoliceofficerCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policeofficer.objects.all()
    serializer_class = PoliceofficerSerializer

    def create(self, request, *args, **kwargs):
        # Extract the data from the request
        fname = request.data.get('fname')
        lname = request.data.get('lname')
        pid = request.data.get('uid')  # Assuming user_id is provided in the request data

        # Get the User instance for the provided user_id
        try:
            user= User.objects.get(pk=pid)
        except User.DoesNotExist:
            return Response({'error': 'User with the provided primary key does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Perform any additional validation or logic here before creating the Police Officer

        # Create the Police Officer object using the provided data and the User instance
        police_officer = Policeofficer.objects.create(
            pid=user,
            fname=fname,
            lname=lname
        )

        # Return a response with the created Police Officer data
        data = {
            'police_officer': PoliceofficerSerializer(police_officer).data,
        }
        return Response(data, status=status.HTTP_201_CREATED)




# police station
class PolicestationDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = PolicestationSerializer


class PolicestationList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = PolicestationSerializer

class PolicestationCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = PolicestationSerializer

    def create(self, request, *args, **kwargs):
        # Extract the data from the request
        ps_name = request.data.get('ps_name')

        # Perform any additional validation or logic here before creating the Police Station

        # Create the Police Station object using the provided data
        policestation = Policestation.objects.create(ps_name=ps_name)

        # Return a response with the created Police Station data
        data = {
            'policestation': PolicestationSerializer(policestation).data,
        }
        return Response(data, status=status.HTTP_201_CREATED)


# Job posting
class JobPostingDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = JobPostingSerializer


class JobPostingList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = JobPostingSerializer


class JobPostingCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

    def create(self, request, *args, **kwargs):
        # Extract the data from the request
        pid = request.data.get('pid')  # Assuming pid of the PoliceOfficer is provided in the request data
        psid = request.data.get('psid')  # Assuming psid of the PoliceStation is provided in the request data
        assigned_on = request.data.get('assigned_on')  # Assuming assigned_on is provided in the request data
        is_active = request.data.get('is_active', 1)  # Set default value to 1 if not provided

        # Get the PoliceOfficer and PoliceStation instances for the provided pid and psid
        try:
            police_officer = Policeofficer.objects.get(pk=pid)
        except Policeofficer.DoesNotExist:
            return Response({'error': 'PoliceOfficer with the provided primary key does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            police_station = Policestation.objects.get(pk=psid)
        except Policestation.DoesNotExist:
            return Response({'error': 'PoliceStation with the provided primary key does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Perform any additional validation or logic here before creating the JobPosting

        # Create the JobPosting object using the provided data and the PoliceOfficer and PoliceStation instances
        job_posting = JobPosting.objects.create(
            pid=police_officer,
            psid=police_station,
            assigned_on=assigned_on,
            is_active=is_active
        )

        # Return a response with the created JobPosting data
        data = {
            'job_posting': JobPostingSerializer(job_posting).data,
        }
        return Response(data, status=status.HTTP_201_CREATED)





# subscribe
class SubscribeDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = SubscribeSerializer


class SubscribeList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = SubscribeSerializer

        
class SubscribeCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer

    def create(self, request, *args, **kwargs):
        psid = request.data.get('psid')
        community_id = request.data.get('community')
        until = request.data.get('until')

        try:
            police_station = Policestation.objects.get(psid=psid)
        except Policestation.DoesNotExist:
            return Response({'error': 'PoliceStation with the provided primary key does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            community = Community.objects.get(community_id=community_id)
        except Community.DoesNotExist:
            return Response({'error': 'Community with the provided primary key does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Perform any additional validation or logic here before creating the Subscribe

        subscribe = Subscribe.objects.create(
            psid=police_station,
            community=community,
            until=until if until else None
        )

        data = {
            'subscribe': SubscribeSerializer(subscribe).data,
        }
        return Response(data, status=status.HTTP_201_CREATED)
