from django.db import models
from Cases.models import Alert 
from PoliceStation.models import JobPosting
from Community.models import Member

# Create your models here.
class CommunityIntervention(models.Model):
    intervention = models.OneToOneField('Intervention', models.DO_NOTHING, primary_key=True)
    initiated_by = models.ForeignKey(Member, models.DO_NOTHING, db_column='initiated_by')

    class Meta:
        managed = False
        db_table = 'community_intervention'

class Intervention(models.Model):
    intervention_id = models.IntegerField(primary_key=True)
    time_initiated = models.DateTimeField(auto_now_add=True)
    alert = models.ForeignKey(Alert, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intervention'

class PoliceIntevention(models.Model):
    intervention = models.OneToOneField(Intervention, models.DO_NOTHING, primary_key=True)
    initiated_by = models.ForeignKey(JobPosting, models.DO_NOTHING, db_column='initiated_by')

    class Meta:
        managed = False
        db_table = 'police_intevention'

class Status(models.Model):
    istatus = models.IntegerField(db_column='iStatus', primary_key=True)  # Field name made lowercase.
    intervention= models.ForeignKey(Intervention, models.DO_NOTHING)
    intervention_status = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'status'
