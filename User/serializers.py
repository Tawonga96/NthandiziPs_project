from rest_framework import serializers
from User.models import User


class User_Serializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = User
        fields = ['uid', 'fname', 'lname', 'pnumber', 'password','email','otp']
        