from rest_framework.response import Response
from rest_framework import status
from Cases.models import Alert, AlertText, AlertMultimedia
from django.shortcuts import render
from Community.models import Member
from Community.serializers import MemberSerializer
from Cases.serializers import *
from rest_framework import generics, permissions, status


class AlertDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class AlertList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class AlertCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

    def create(self, request, *args, **kwargs):
        # Extract the data from the request
        code = request.data.get('code')
        author= request.data.get('author') 
        origin = request.data.get('origin', '')
        a_type = request.data.get('a_type', '')
        false_alarm = request.data.get('false_alarm', None)
        voided_by = request.data.get('voided_by', None)
        closed_at = request.data.get('closed_at', None)
        closed_by = request.data.get('closed_by', None)

        # Check if required fields are provided and not empty
        if not code or not author:
            return Response({'error': 'Please provide both "code" and "author" values.'}, status=status.HTTP_400_BAD_REQUEST)

        # Get the Member instance for the author of the alert
        try:
            from Community.models import Member  # Import Member model here
            author_instance = Member.objects.get(pk=author)
        except Member.DoesNotExist:
            return Response({'error': 'Member with the provided primary key does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Perform any additional validation or logic here before creating the Alert

        # Create the Alert object using the provided data and the author Member instance
        alert = Alert.objects.create(
            # a_time=a_time,
            code=code,
            author=author_instance,
            origin=origin,
            a_type=a_type,
            false_alarm=false_alarm,
            voided_by=voided_by,
            closed_at=closed_at,
            closed_by=closed_by
        )

         # Create AlertText instance and link it to the Alert using the alert_id
        alert_text_message = request.data.get('alert_text_message', '')  # Assuming the message is provided in the request data
        alert_text = AlertText.objects.create(
            alert_id=alert,
            message=alert_text_message
        )

        # Create AlertMultimedia instance and link it to the Alert using the alert_id
        alert_multimedia_path = request.data.get('alert_multimedia_path', '')  # Assuming the path is provided in the request data
        alert_multimedia_ext = request.data.get('alert_multimedia_ext', '')  # Assuming the extension is provided in the request data
        alert_multimedia = AlertMultimedia.objects.create(
            alert_id=alert,  # Use alert instance here, not alert_id
            path=alert_multimedia_path,
            ext=alert_multimedia_ext
        )

          # Return a response with the created Alert data and associated AlertText and AlertMultimedia data
        data = {
            'alert': AlertSerializer(alert).data,
            'alert_text': AlertTextSerializer(alert_text).data,
            'alert_multimedia': AlertMultimediaSerializer(alert_multimedia).data,
        }
        # Return a response with the created Alert data
        # return Response(AlertSerializer(alert).data, status=status.HTTP_201_CREATED)
        return Response(data, status=status.HTTP_201_CREATED)





class AlertTextDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertText.objects.all()
    serializer_class = AlertTextSerializer

class AlertTextList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertText.objects.all()
    serializer_class = AlertTextSerializer

class AlertTextCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertText.objects.all()
    serializer_class = AlertTextSerializer

    def create(self, request, *args, **kwargs):
        # Extract the data from the request
        alert_id = request.data.get('alert_id')
        message = request.data.get('message')

        # Get the Alert instance for the provided alert_id
        try:
            alert_instance = Alert.objects.get(pk=alert_id)
        except Alert.DoesNotExist:
            return Response({'error': 'Alert with the provided primary key does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Create the AlertText instance and link it to the Alert using the alert_id
        alert_text = AlertText.objects.create(
            alert=alert_instance,
            message=message
        )

        # Return a response with the created AlertText data
        return Response(AlertTextSerializer(alert_text).data, status=status.HTTP_201_CREATED)







class AlertTextMultimediaDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertMultimedia.objects.all()
    serializer_class = AlertMultimediaSerializer


class AlertTextMultimediaList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertMultimedia.objects.all()
    serializer_class = AlertMultimediaSerializer

class AlertMultimediaCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertMultimedia.objects.all()
    serializer_class = AlertMultimediaSerializer

    def create(self, request, *args, **kwargs):
        # Extract the data from the request
        alert_id = request.data.get('alert_id')
        path = request.data.get('path')
        ext = request.data.get('ext')

        # Get the Alert instance for the provided alert_id
        try:
            alert_instance = Alert.objects.get(pk=alert_id)
        except Alert.DoesNotExist:
            return Response({'error': 'Alert with the provided primary key does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Perform any additional validation or logic here before creating the AlertMultimedia

        # Create the AlertMultimedia object using the provided data and the Alert instance
        alert_multimedia = AlertMultimedia.objects.create(
            alert=alert_instance,
            path=path,
            ext=ext
        )

        # Return a response with the created AlertMultimedia data
        data = {
            'alert_multimedia': AlertMultimediaSerializer(alert_multimedia).data,
        }
        return Response(data, status=status.HTTP_201_CREATED)


class MemberList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Member.objects.all()
    serializer_class = MemberSerializer