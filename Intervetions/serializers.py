from rest_framework import serializers
from Intervetions.models import CommunityIntervention, Intervention, PoliceIntevention, Status


class CommunityIntervetion_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = CommunityIntervention
        fields = ['Intervention', 'initiated_by']


class Intervetion_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Intervention
        fields = ['Intervention_id', 'time_initiated', 'alert']


class PoliceIntervetion_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = PoliceIntevention
        fields = ['intervention', 'initiated_by']

class Status_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Status
        fields = ['istatus', 'Intervetion', 'status', 'updated_on']

