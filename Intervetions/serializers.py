from rest_framework import serializers
# from Cases.serializers import AlertSerializer
from Intervetions.models import CommunityIntervention, Intervention, PoliceIntevention, Status


class CommunityIntervetionSerializer(serializers.ModelSerializer):
     
     class Meta:
        model = CommunityIntervention
      #   fields = ['Intervention', 'initiated_by']
        fields = ['initiated_by'] 


class InterventionSerializer(serializers.ModelSerializer):
      community_intervention = CommunityIntervetionSerializer(many=False, read_only=True)

      class Meta:
         model = Intervention
         fields = ['intervention_id','alert','community_intervention']


class PoliceIntervetionSerializer(serializers.ModelSerializer):
     class Meta:
        model = PoliceIntevention
        fields = ['intervention', 'initiated_by']

class StatusSerializer(serializers.ModelSerializer):
     class Meta:
        model = Status
        fields = ['intervention', 'intervention_status', 'updated_on']
