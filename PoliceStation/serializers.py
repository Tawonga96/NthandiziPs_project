from rest_framework import serializers
from PoliceStation.models import JobPosting, Policeofficer, Policestation, Subscribe

class JobPostingSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = JobPosting
        fields = ['posting_id', 'pid', 'psid', 'assigned_on']


class  PoliceofficerSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Policeofficer
        fields = ['pid', 'fname', 'lname']


class  PolicestationSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Policestation
        fields = ['psid', 'ps_name']

 
class SubscribeSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
      model = Subscribe
      fields = ['subcription_id','psid',  'community', 'subscribed_on','until']

         
    