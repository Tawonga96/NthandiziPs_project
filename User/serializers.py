from rest_framework import serializers
from User.models import User


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


class UserSerializer(serializers.ModelSerializer):
    login = LoginSerializer(required=False)
    register =RegisterSerializer(required=False)
  
    class Meta:   
        model = User
        fields = ['fname', 'lname', 'pnumber', 'password','email','otp','is_active','login','register']












# class UserSerializer(serializers.ModelSerializer):
#       login = LoginSerializer(required=False)

#       class Meta:   
#         model = User
#         fields = ['fname', 'lname', 'pnumber', 'password','email','otp','is_active','login']
