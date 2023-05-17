from rest_framework import serializers
from Community.models import Citizen, Community, CommunityLeader, Household, Housemember, Member


class CitizenSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Citizen
        fields = ['cid', 'occupation']



class CommunitySerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Community
        fields = ['community_id', 'district', 'comm_name','area,date_added']


class CommunityLeaderSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = CommunityLeader
        fields = ['leader', 'community','elected_on']



class HouseholdSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Household
        fields = ['hhid', 'date_added','hh_name']


class HousememberSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Housemember
        fields = ['h_id', 'mid','hhid','date_joined']
        

class MemberSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Member
        fields = ['mid', 'cid','community','date_joined','date_joined','left_on', 'citizen_typ']