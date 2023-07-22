from django.shortcuts import render
from Cases.models import Alert
from Community.models import Member
from Intervetions.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from PoliceStation.models import JobPosting



# Create your views here.
class InterventionDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer


class InterventionList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer


class InterventionCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = InterventionSerializer

    def create(self, request, *args, **kwargs):
        # Extract the data from the request
        intervention_id = request.data.get('intervention_id')
        alert_id = request.data.get('alert')
        initiated_by = request.data.get('initiated_by')

        # Get the Alert instance for the provided alert_id
        try:
            alert_instance = Alert.objects.get(alert_id=alert_id)
        except Alert.DoesNotExist:
            return Response({'error': 'Alert with the provided alert_id does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Create the Intervention object using the provided data and the Alert instance
        intervention = Intervention.objects.create(
            intervention_id=intervention_id,
            alert=alert_instance
        )

        # Check if 'initiated_by' is provided in the request data
        if initiated_by is not None:
            # Get the Member instance for the provided initiated_by_id
            try:
                initiated_by_instance = Member.objects.get(cid=initiated_by)
            except Member.DoesNotExist:
                return Response({'error': 'Member with the provided initiated_by_id does not exist.'},
                                status=status.HTTP_400_BAD_REQUEST)

            # Create the CommunityIntervention object using the provided data and the Member instance
            community_intervention = CommunityIntervention.objects.create(
                intervention=intervention,
                initiated_by=initiated_by_instance
            )

        # Return a response with the created Intervention data
        return Response(InterventionSerializer(intervention).data, status=status.HTTP_201_CREATED)





class PoliceInterventionCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PoliceIntervetionSerializer

    def create(self, request, *args, **kwargs):
        # Extract the data from the request
        intervention_id = request.data.get('intervention_id')
        initiated_by = request.data.get('initiated_by')

        # Get the Intervention instance for the provided intervention_id
        try:
            intervention_instance = Intervention.objects.get(intervention_id=intervention_id)
        except Intervention.DoesNotExist:
            return Response({'error': 'Intervention with the provided intervention_id does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check if 'initiated_by' is provided in the request data
        if initiated_by is not None:
            # Get the JobPosting instance for the provided initiated_by_id (police officer)
            try:
                initiated_by_instance = JobPosting.objects.get(id=initiated_by)
            except JobPosting.DoesNotExist:
                return Response({'error': 'JobPosting with the provided initiated_by_id does not exist.'},
                                status=status.HTTP_400_BAD_REQUEST)

            # Create the PoliceIntervention object using the provided data and the Intervention and JobPosting instances
            police_intervention = PoliceIntevention.objects.create(
                intervention=intervention_instance,
                initiated_by=initiated_by_instance
            )

        # Return a response with the created PoliceIntervention data
        return Response(PoliceIntervetionSerializer(police_intervention).data, status=status.HTTP_201_CREATED)
    




class StatusDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = StatusSerializer

    def create(self, request, *args, **kwargs):
        # Extract the data from the request
        intervention_id = request.data.get('intervention')
        intervention_status = request.data.get('intervention_status')
        # updated_on = request.data.get('updated_on')

        # Get the Intervention instance for the provided intervention_id
        try:
            intervention_instance = Intervention.objects.get(intervention_id=intervention_id)
        except Intervention.DoesNotExist:
            return Response({'error': 'Intervention with the provided intervention_id does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Create the Status object using the provided data and the Intervention instance
        status = Status.objects.create(
            intervention=intervention_instance,
            intervention_status=intervention_status,
            # updated_on=updated_on
        )

        # Return a response with the created Status data
        return Response(StatusSerializer(status).data, status=status.HTTP_201_CREATED)
   