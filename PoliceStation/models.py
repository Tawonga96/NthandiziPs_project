from django.db import models
from Community.models import Community
from User.models import User

# Create your models here.
class JobPosting(models.Model):
    posting_id = models.IntegerField(primary_key=True)
    pid = models.ForeignKey('Policeofficer', models.DO_NOTHING, db_column='pid')
    psid = models.ForeignKey('Policestation', models.DO_NOTHING, db_column='psid')
    assigned_on = models.DateTimeField()
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'job_posting'

class Policeofficer(models.Model):
    pid = models.OneToOneField(User, models.DO_NOTHING, db_column='pid', primary_key=True)
    fname = models.CharField(max_length=35)
    lname = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'policeofficer'


class Policestation(models.Model):
    psid = models.IntegerField(primary_key=True)
    ps_name = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'policestation'

class Subscribe(models.Model):
    subscription_id = models.IntegerField(primary_key=True)
    psid = models.ForeignKey(Policestation, models.DO_NOTHING, db_column='psid')
    community = models.ForeignKey(Community, models.DO_NOTHING)
    suscribed_on = models.DateTimeField()
    until = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscribe'

