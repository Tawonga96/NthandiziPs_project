from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from Cases.serializers import *
from rest_framework import generics, permissions


class AlertDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class AlertList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class AlertTextDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertText.objects.all()
    serializer_class = AlertTextSerializer

class AlertTextList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertText.objects.all()
    serializer_class = AlertTextSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            # Extract the message and code from the request data
            message = serializer.validated_data['message']
            code = request.data.get('code')  # Extract the code field

            # Create a new Alert instance and set the code
            alert = Alert.objects.create(code=code)

            # Set the foreign key relationship
            serializer.validated_data['alert'] = alert

            # Save the serializer to create the AlertText instance
            self.perform_create(serializer)

            # Return success response
            return Response({'message': 'AlertText created successfully.'}, status=status.HTTP_201_CREATED)


        except Alert.DoesNotExist:
            # Return error response if the associated Alert instance doesn't exist
            return Response({'message': 'Associated Alert not found.'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Return error response for any other exceptions
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)



class AlertTextMultimediaDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertMultimedia.objects.all()
    serializer_class = AlertMultimediaSerializer


class AlertTextMultimediaList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AlertMultimedia.objects.all()
    serializer_class = AlertMultimediaSerializer
