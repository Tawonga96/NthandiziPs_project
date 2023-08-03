from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework import status
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from Cases.models import Alert, AlertText, AlertMultimedia
from Cases.serializers import *
from Community.models import Member
from Community.serializers import MemberSerializer


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
        author_id = request.data.get('author')  # Assuming 'author' is the primary key of the Member model
        a_type = request.data.get('a_type')  # Get the value of a_type from the request

        # Check if required fields are provided and not empty
        if not code or not author_id or not a_type:
            return Response({'error': 'Please provide values for all empty fields..'}, status=status.HTTP_400_BAD_REQUEST)

        # Get the Member instance for the author of the alert
        try:
            from Community.models import Member  # Import Member model here
            author_instance = Member.objects.get(pk=author_id)
        except Member.DoesNotExist:
            return Response({'error': 'Member with the provided primary key does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Create the Alert object using the provided data and the author Member instance
        alert = Alert.objects.create(
            code=code,
            author=author_instance,
            a_type=a_type  # Set the a_type explicitly as per the request
        )

        # Check the value of a_type and create the corresponding Alert object
        if a_type == 'Alert_text':
            message = request.data.get('message')

            if not message:
                return Response({'error': 'Please provide message you want to send'}, status=status.HTTP_400_BAD_REQUEST)

            alert_text = AlertText.objects.create(
                alert_id=alert.alert_id,
                message=message
            )
            alert_text_serializer = AlertTextSerializer(alert_text)
            data = {
                'alert': AlertSerializer(alert).data,
                'alert_text': alert_text_serializer.data,
            }
        elif a_type == 'Alert_multimedia':
            path = request.data.get('path')
            ext = request.data.get('ext')

            alert_multimedia = AlertMultimedia.objects.create(
                alert_id=alert.alert_id,
                path=path,
                ext=ext
            )
            alert_multimedia_serializer = AlertMultimediaSerializer(alert_multimedia)
            data = {
                'alert': AlertSerializer(alert).data,
                'alert_multimedia': alert_multimedia_serializer.data,
            }

            # Now handle the multimedia (video) upload and associate the video path with the AlertMultimedia object
            video_file = request.FILES.get('video')
            if video_file:
                fs = FileSystemStorage()
                filename = fs.save(video_file.name, video_file)
                video_path = fs.url(filename)
                alert_multimedia.path = video_path
                alert_multimedia.ext = 'video'  # Assuming the extension is 'video', you can change it accordingly
                alert_multimedia.save()

              # Now handle the multimedia (image) upload and associate the image path with the AlertMultimedia object
            image_file = request.FILES.get('image')
            if image_file:
                fs = FileSystemStorage()
                filename = fs.save(image_file.name, image_file)
                image_path = fs.url(filename)
                alert_multimedia.path = image_path
                alert_multimedia.ext = 'image'  # Assuming the extension is 'image', you can change it accordingly
                alert_multimedia.save()

            # Check if either video or image file is provided, return an error response if none are provided
            if not video_file and not image_file:
                return Response({'error': 'Video or Image file is missing'}, status=status.HTTP_400_BAD_REQUEST)


            else:
                # If the video file is not provided, return an error response
                return Response({'error': 'Video file is missing'}, status=status.HTTP_400_BAD_REQUEST)

            
        else:
            data = {
                'alert': AlertSerializer(alert).data,
            }

        return Response(data, status=status.HTTP_201_CREATED)



class AlertTextDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertText.objects.all()
    serializer_class = AlertTextSerializer

class AlertTextList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertText.objects.all()
    serializer_class = AlertTextSerializer

class AlertTextMultimediaDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertMultimedia.objects.all()
    serializer_class = AlertMultimediaSerializer


class AlertTextMultimediaList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertMultimedia.objects.all()
    serializer_class = AlertMultimediaSerializer