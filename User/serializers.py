from rest_framework import serializers
from User.models import User


class UserSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ['uid', 'fname', 'lname', 'pnumber', 'password','email','otp']
        