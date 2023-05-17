from django.shortcuts import render
from Cases.serializers import *
from rest_framework import generics, permissions


class AlertDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class AlertList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class AlertTextDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertText.objects.all()
    serializer_class = AlertTextSerializer

class AlertTextList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertText.objects.all()
    serializer_class = AlertTextSerializer


class AlertTextMultimediaDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertMultimedia.objects.all()
    serializer_class = AlertMultimediaSerializer


class AlertTextMultimediaList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertMultimedia.objects.all()
    serializer_class = AlertMultimediaSerializer
