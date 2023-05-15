from django.db import models
from User.models import User

# Create your models here.
class Citizen(models.Model):
    cid = models.OneToOneField(User, models.DO_NOTHING, db_column='cid', primary_key=True)
    occupation = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'citizen'

class Community(models.Model):
    community_id = models.IntegerField(primary_key=True)
    district = models.CharField(max_length=30)
    comm_name = models.CharField(max_length=35)
    area = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'community'

class CommunityLeader(models.Model):
    leader = models.OneToOneField('Member', models.DO_NOTHING, primary_key=True)
    community = models.ForeignKey(Community, models.DO_NOTHING)
    elected_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'community_leader'


class Household(models.Model):
    hhid = models.IntegerField(primary_key=True)
    date_added = models.DateTimeField()
    hh_name = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'household'

class Housemember(models.Model):
    hm_id = models.IntegerField(primary_key=True)
    mid = models.ForeignKey('Member', models.DO_NOTHING, db_column='mid')
    hhid = models.ForeignKey(Household, models.DO_NOTHING, db_column='hhid')
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'housemember'

class Member(models.Model):
    mid = models.IntegerField(primary_key=True)
    cid = models.ForeignKey(Citizen, models.DO_NOTHING, db_column='cid')
    community = models.ForeignKey(Community, models.DO_NOTHING)
    date_joined = models.DateTimeField()
    left_on = models.DateTimeField(blank=True, null=True)
    citizen_typ = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'member'
