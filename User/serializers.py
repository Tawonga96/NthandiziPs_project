from rest_framework import serializers
from User.models import User
from Community.serializers import CommunityLeaderSerializer


class LoginSerializer(serializers.Serializer):
    fname = serializers.CharField()
    password = serializers.CharField()


class RegisterSerializer(serializers.Serializer):
    fname = serializers.CharField()
    lname = serializers.CharField()
    pnumber = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    otp = serializers.CharField()

class CommunityLeaderSerializer(serializers.Serializer):
    fname = serializers.CharField()
    password = serializers.CharField() 
    # is_community_leader = serializers.BooleanField()


class UserSerializer(serializers.ModelSerializer):
    login = LoginSerializer(required=False)
    register =RegisterSerializer(required=False)
    community_leader = CommunityLeaderSerializer(required=False)
  
    class Meta:   
        model = User
        fields = ['fname', 'lname', 'pnumber', 'password','email','otp','is_community_leader','is_active','login','register','community_leader']












# class UserSerializer(serializers.ModelSerializer):
#       login = LoginSerializer(required=False)

#       class Meta:   
#         model = User
#         fields = ['fname', 'lname', 'pnumber', 'password','email','otp','is_active','login']
