from rest_framework import serializers
from Cases.models import Alert ,AlertText,AlertMultimedia
from Community.models import Member
from Intervetions.serializers import InterventionSerializer  # Import Member model here


class AlertSerializer(serializers.ModelSerializer):
        class Meta:
                model = Alert
                fields = ['a_time','code', 'author','origin','a_type','false_alarm','voided_by','closed_at','closed_by']


class AlertTextSerializer(serializers.ModelSerializer):
     class Meta:
        model = AlertText
        fields = ['message']


class AlertMultimediaSerializer(serializers.ModelSerializer):
     class Meta:
        model = AlertMultimedia
        fields = ['path','ext']


# class MemberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Member
#         fields = ['cid', 'community_id', 'date_joined', 'left_on', 'citizen_typ']
