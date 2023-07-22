from rest_framework import serializers
from PoliceStation.models import JobPosting, Policeofficer, Policestation, Subscribe
from Community.serializers import CommunitySerializer


class JobPostingSerializer(serializers.ModelSerializer):
     class Meta:
        model = JobPosting
        fields = ['posting_id', 'pid', 'psid', 'assigned_on']


class  PoliceofficerSerializer(serializers.ModelSerializer):

     class Meta:
        model = Policeofficer
        fields = ['pid', 'fname', 'lname']


class  PolicestationSerializer(serializers.ModelSerializer):
     class Meta:
        model = Policestation
        fields = ['ps_name']

 
class SubscribeSerializer(serializers.ModelSerializer):
     # until = serializers.DateTimeField(required=False, allow_null=True)

     class Meta:
          model = Subscribe
          fields = ['psid', 'community', 'subscribed_on','until']

 