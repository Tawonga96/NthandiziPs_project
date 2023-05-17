from django.shortcuts import render
from PoliceStation.serializers import *
from rest_framework import generics, permissions

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


# police station
class PolicestationDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = PolicestationSerializer


class PolicestationList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = PolicestationSerializer


# Job posting
class JobPostingDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = JobPostingSerializer


class JobPostingList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = JobPostingSerializer


# subscribe
class SubscribeDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = SubscribeSerializer


class SubscribeList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Policestation.objects.all()
    serializer_class = SubscribeSerializer


