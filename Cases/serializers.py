from rest_framework import serializers
from Cases.models import Alert ,AlertText,AlertMultimedia


class Citizen_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Alert
        fields = ['alert_id', 'code', 'author','origin','a_type','false_alarm','voided_by','closed_at','closed_by']


class AlertText_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = AlertText
        fields = ['alert', 'message']


class AlertMultimedia_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = AlertMultimedia
        fields = ['alert', 'path','ext']

