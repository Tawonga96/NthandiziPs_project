from rest_framework import serializers
from Community.models import Citizen, Community, CommunityLeader, Household, Housemember, Member
from User.models import User
from Community.serializers import *


class CitizenSerializer(serializers.ModelSerializer):

      class Meta:
        model = Citizen
        fields = ['cid', 'occupation','user']


class CommunitySerializer(serializers.ModelSerializer):
     class Meta:
        model = Community
        fields = ['community_id','district', 'comm_name','area','date_added']


class CommunityLeaderSerializer(serializers.ModelSerializer):
      class Meta:
        model = CommunityLeader
        fields = ['leader_id', 'community_id','elected_on']



class HouseholdSerializer(serializers.ModelSerializer):
     class Meta:
        model = Household
        fields = ['hhid', 'date_added','hh_name']


class HousememberSerializer(serializers.ModelSerializer):
     class Meta:
        model = Housemember
        fields = ['h_id', 'mid','hhid','date_joined']
        

class MemberSerializer(serializers.ModelSerializer):
     
     class Meta:
        model = Member
        fields = ['mid','cid','community','is_active','date_joined','left_on','citizen_typ']