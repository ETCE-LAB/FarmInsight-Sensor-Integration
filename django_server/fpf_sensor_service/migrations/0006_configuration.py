# Generated by Django 5.1.2 on 2024-11-24 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpf_sensor_service', '0005_alter_sensorconfig_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True)),
                ('value', models.CharField(max_length=1024)),
            ],
        ),
    ]
