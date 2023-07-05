from rest_framework import serializers
from User.models import User
from Community.serializers import CommunityLeaderSerializer
from Community.serializers import CommunitySerializer



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

class UserSerializer(serializers.ModelSerializer):
    login = LoginSerializer(required=False)
    register =RegisterSerializer(required=False)
    community_leader = CommunityLeaderSerializer(required=False)
    is_community_leader = serializers.BooleanField(required=False, default=False)
    community = CommunitySerializer(required=False)  # Import and include the CommunitySerializer here

  
    class Meta:   
        model = User
        fields = ['fname', 'lname', 'pnumber', 'password','email','otp','is_community_leader','is_active','login','register','community_leader','community']












# class UserSerializer(serializers.ModelSerializer):
#       login = LoginSerializer(required=False)

#       class Meta:   
#         model = User
#         fields = ['fname', 'lname', 'pnumber', 'password','email','otp','is_active','login']
