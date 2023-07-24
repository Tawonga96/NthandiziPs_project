from rest_framework import serializers
from User.models import User

class LoginSerializer(serializers.Serializer):
    fname = serializers.CharField()
    password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    # login = LoginSerializer(required=False)

    class Meta:   
        model = User
        fields = ['uid','fname', 'lname', 'pnumber', 'password','email','date_joined']
       

