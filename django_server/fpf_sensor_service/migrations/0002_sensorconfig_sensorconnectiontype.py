# Generated by Django 5.1.2 on 2024-11-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpf_sensor_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensorconfig',
            name='sensorConnectionType',
            field=models.CharField(default='PinConnection', max_length=256),
            preserve_default=False,
        ),
    ]