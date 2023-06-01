from rest_framework import serializers
from Cases.models import Alert ,AlertText,AlertMultimedia


class AlertSerializer(serializers.ModelSerializer):
      class Meta:
        model = Alert
        fields = ['alert_id', 'code', 'author','origin','a_type','false_alarm','voided_by','closed_at','closed_by']


class AlertTextSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = AlertText
        fields = ['alert', 'message']


class AlertMultimediaSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = AlertMultimedia
        fields = ['alert', 'path','ext']

