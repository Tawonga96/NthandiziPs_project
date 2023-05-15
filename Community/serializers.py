from rest_framework import serializers
from Community.models import Citizen, Community, CommunityLeader, Household, Housemember, Member


class Citizen_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Citizen
        fields = ['cid', 'occupation']



class Community_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Community
        fields = ['community_id', 'district', 'comm_name','area,date_added']


class CommunityLeader_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = CommunityLeader
        fields = ['leader', 'community','elected_on']



class Household_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Household
        fields = ['hhid', 'date_added','hh_name']


class Housemember_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Housemember
        fields = ['h_id', 'mid','hhid','date_joined']
        

class Member_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Member
        fields = ['mid', 'cid','community','date_joined','date_joined','left_on', 'citizen_typ']