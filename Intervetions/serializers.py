from rest_framework import serializers
from Intervetions.models import CommunityIntervention, Intervention, PoliceIntevention, Status


class CommunityIntervetionSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = CommunityIntervention
        fields = ['Intervention', 'initiated_by']


class IntervetionSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Intervention
        fields = ['Intervention_id', 'time_initiated', 'alert']


class PoliceIntervetionSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = PoliceIntevention
        fields = ['intervention', 'initiated_by']

class StatusSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Status
        fields = ['istatus', 'Intervetion', 'status', 'updated_on']

