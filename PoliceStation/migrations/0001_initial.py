# Generated by Django 4.1.5 on 2023-05-14 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('posting_id', models.IntegerField(primary_key=True, serialize=False)),
                ('assigned_on', models.DateTimeField()),
                ('is_active', models.IntegerField()),
            ],
            options={
                'db_table': 'job_posting',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Policeofficer',
            fields=[
                ('pid', models.OneToOneField(db_column='pid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='User.user')),
                ('fname', models.CharField(max_length=35)),
                ('lname', models.CharField(max_length=35)),
            ],
            options={
                'db_table': 'policeofficer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Policestation',
            fields=[
                ('psid', models.IntegerField(primary_key=True, serialize=False)),
                ('ps_name', models.CharField(max_length=35)),
            ],
            options={
                'db_table': 'policestation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('subscription_id', models.IntegerField(primary_key=True, serialize=False)),
                ('suscribed_on', models.DateTimeField()),
                ('until', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'subscribe',
                'managed': False,
            },
        ),
    ]
