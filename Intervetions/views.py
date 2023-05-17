from django.shortcuts import render
from Intervetions.serializers import *
from rest_framework import generics, permissions


# Create your views here.
class InterventionDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Intervention.objects.all()
    serializer_class = IntervetionSerializer


class InterventionList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Intervention.objects.all()
    serializer_class = IntervetionSerializer

    

