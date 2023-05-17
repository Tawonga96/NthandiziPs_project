from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    pnumber = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    otp = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'