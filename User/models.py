from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class User(models.Model):
    uid = models.IntegerField(primary_key=True, auto_created=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    pnumber = models.CharField(max_length=15)
    password = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    otp = models.BigIntegerField()
    is_community_leader = models.BooleanField(default=False)
    is_active = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'user'