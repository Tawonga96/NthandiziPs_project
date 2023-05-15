from rest_framework import serializers
from PoliceStation.models import JobPosting, Policeofficer, Policestation, Subscribe

class JobPosting_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = JobPosting
        fields = ['posting_id', 'pid', 'psid', 'assigned_on']


class  Policeofficer_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Policeofficer
        fields = ['pid', 'fname', 'lname']


class  Policestation_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Policestation
        fields = ['psid', 'ps_name']


class JobPosting_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = JobPosting
        fields = ['posting_id', 'pid', 'psid', 'assigned_on']
 
 
class Subscribe_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Subscribe
        fields = ['subcription_id','psid',  'community', 'subscribed_on','until']
  
         
    