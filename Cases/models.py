from django.db import models
from Community.models import Member


# Create your models here.
class Alert(models.Model):
    alert_id = models.IntegerField(primary_key=True, auto_created=True)
    a_time = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=128)
    author = models.ForeignKey(Member, models.DO_NOTHING, db_column='author')
    origin = models.TextField(blank=True, null=True)  # This field type is a guess.
    a_type = models.CharField(max_length=20, null=True, blank=True)
    false_alarm = models.IntegerField(blank=True, null=True)
    voided_by = models.IntegerField(blank=True, null=True)
    closed_at = models.DateTimeField(blank=True, null=True)
    closed_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alert'


class AlertText(models.Model):
    alert= models.OneToOneField(Alert, models.DO_NOTHING, primary_key=True)
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'alert_text'


class AlertMultimedia(models.Model):
    alert = models.OneToOneField(Alert, models.DO_NOTHING, primary_key=True)
    path = models.IntegerField()
    ext = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alert_multimedia'
