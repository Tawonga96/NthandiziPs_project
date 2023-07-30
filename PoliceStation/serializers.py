from rest_framework import serializers
from PoliceStation.models import JobPosting, Policeofficer, Policestation, Subscribe
from Community.serializers import CommunitySerializer


class JobPostingSerializer(serializers.ModelSerializer):
     class Meta:
        model = JobPosting
        fields = ['pid', 'psid', 'assigned_on']


class  PoliceofficerSerializer(serializers.ModelSerializer):

     class Meta:
        model = Policeofficer
        fields = ['pid', 'position', 'user']


class  PolicestationSerializer(serializers.ModelSerializer):
     class Meta:
        model = Policestation
        fields = ['psid','ps_name']

 
class SubscribeSerializer(serializers.ModelSerializer):
     # until = serializers.DateTimeField(required=False, allow_null=True)

     class Meta:
          model = Subscribe
          fields = ['psid', 'community', 'subscribed_on','until']

 