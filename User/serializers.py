from rest_framework import serializers
from User.models import User
from Community.models import Citizen 


class UserSerializer(serializers.ModelSerializer):
    # uid = serializers.IntegerField(read_only=True)  # Set read_only to True

    class Meta:   
        model = User
        fields = ['fname', 'lname', 'pnumber', 'password','email']
       

