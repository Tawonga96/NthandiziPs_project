from django.db import models
import string
import random


def generate_random_uid():
    # Generate a random 6-character alphanumeric value for uid
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))

class User(models.Model):
    uid = models.CharField(primary_key=True, default=generate_random_uid, unique=True, editable=False, max_length=6)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    pnumber = models.CharField(max_length=15)
    password = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    otp = models.BigIntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'user'
    


    