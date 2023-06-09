# Generated by Django 4.1.5 on 2023-05-14 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('alert_id', models.IntegerField(primary_key=True, serialize=False)),
                ('a_time', models.DateTimeField()),
                ('code', models.CharField(max_length=128)),
                ('origin', models.TextField(blank=True, null=True)),
                ('a_type', models.CharField(max_length=20)),
                ('false_alarm', models.IntegerField()),
                ('voided_by', models.IntegerField()),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
                ('closed_by', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'alert',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AlertMultimedia',
            fields=[
                ('alert', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Cases.alert')),
                ('path', models.IntegerField()),
                ('ext', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'alert_multimedia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AlertText',
            fields=[
                ('alert', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Cases.alert')),
                ('message', models.TextField()),
            ],
            options={
                'db_table': 'alert_text',
                'managed': False,
            },
        ),
    ]
