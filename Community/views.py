from django.shortcuts import render
from Community.serializers import *
from rest_framework import generics,permissions

# Create your views here.

class CommunityDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CommunityList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CitizenDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = CitizenSerializer


class CitizenList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = CitizenSerializer


class CommunityLeaderDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = CommunityLeaderSerializer


class CommunityLeaderList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Community.objects.all()
    serializer_class = CommunityLeaderSerializer

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

