import random
from .models import SensorConfig, SensorMeasurement
import requests
from django.conf import settings


def generate_measurement(sensor):
    """
    Dummy function to mimic a sensor measurement
    Stores a random measurement value in the sqlite db SensorMeasurement
    :param sensor: Sensor to measure
    """
    try:
        db_sensor = SensorConfig.objects.get(sensorId=sensor.sensorId)
        SensorMeasurement.objects.create(
            sensorId=db_sensor.sensorId,
            value=random.uniform(20.0, 100.0)
        )
    except SensorConfig.DoesNotExist:
        print(f"SensorConfig with sensorId {sensor.sensorId} does not exist.")
    except ValueError as e:
        print(f"Invalid UUID format: {e}")


def send_measurements(sensorId):
    """
    For given sensor, try to send all measurements to central app.
    If succeeded, delete entries from local database.
    :param sensorId: GUID of sensor
    """
    measurements = SensorMeasurement.objects.filter(sensorId=sensorId)
    if measurements.exists():
        data = [
            {'measuredAt': m.measuredAt.isoformat(), 'value': m.value}
            for m in measurements
        ]

        url = f"{settings.MEASUREMENTS_BASE_URL}/measurements/{sensorId}"
        response = requests.post(url, json={'measurements': data})

        if response.status_code == 200:
            measurements.delete()
        else:
            print('Error sending measurements, will retry.')