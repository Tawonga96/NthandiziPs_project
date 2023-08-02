from rest_framework import serializers
from Community.serializers import CitizenSerializer, MemberSerializer
from User.models import User

class LoginSerializer(serializers.Serializer):
    fname = serializers.CharField()
    password = serializers.CharField()

class AccountActivationSerializer(serializers.Serializer):
    uid = serializers.CharField()
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:   
        model = User
        fields = ['uid','fname', 'lname', 'pnumber','password','email','date_joined']
       

