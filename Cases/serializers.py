from rest_framework import serializers
from Cases.models import Alert ,AlertText,AlertMultimedia
from Community.models import Member
from Intervetions.serializers import InterventionSerializer  # Import Member model here


class AlertSerializer(serializers.ModelSerializer):
      # update alertSerilaizer
        # interventions = serializers.SerializerMethodField()

        # def get_interventions(self, obj):
        #         interventions = obj.intervention_set.all()
        #         return IntervetionSerializer(interventions, many=True).data


        class Meta:
                model = Alert
                fields = ['a_time','code', 'author','origin','a_type','false_alarm','voided_by','closed_at','closed_by']


class AlertTextSerializer(serializers.ModelSerializer):
     class Meta:
        model = AlertText
        fields = ['alert_id', 'message']


class AlertMultimediaSerializer(serializers.ModelSerializer):
     class Meta:
        model = AlertMultimedia
        fields = ['alert_id', 'path','ext']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['cid', 'community_id', 'date_joined', 'left_on', 'citizen_typ']
