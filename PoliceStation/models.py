from django.db import models
from Community.models import Community
from User.models import User, generate_random_uid

# Create your models here.
class JobPosting(models.Model):
    posting_id = models.IntegerField(primary_key=True)
    pid = models.ForeignKey('Policeofficer', models.DO_NOTHING, db_column='pid', to_field='pid')
    psid = models.ForeignKey('Policestation', models.DO_NOTHING, db_column='psid')
    assigned_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'job_posting'

class Policeofficer(models.Model):
    # pid = models.OneToOneField(User, models.DO_NOTHING, db_column='pid', primary_key=True)
    pid = models.CharField(primary_key=True, max_length=6, unique=True, editable=False, default=generate_random_uid)  # Store the pid as a string
    position = models.CharField(max_length=35)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='policeofficer')
   

    class Meta:
        managed = False
        db_table = 'policeofficer'


class Policestation(models.Model):
    psid = models.IntegerField(primary_key=True,auto_created=True)
    ps_name = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'policestation'

class Subscribe(models.Model):
    subscription_id = models.IntegerField(primary_key=True)
    psid = models.ForeignKey(Policestation, models.DO_NOTHING, db_column='psid')
    community = models.ForeignKey(Community, models.DO_NOTHING)
    subscribed_on = models.DateTimeField(auto_now_add=True)
    until = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscribe'

