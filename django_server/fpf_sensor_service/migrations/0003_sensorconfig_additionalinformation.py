# Generated by Django 5.1.2 on 2024-11-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpf_sensor_service', '0002_sensorconfig_sensorconnectiontype'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensorconfig',
            name='additionalInformation',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]
