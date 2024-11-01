import uuid
from django.db import models
from .sensor_config import SensorConfig


class SensorMeasurement(models.Model):
    """
    SensorMeasurement model with the id as a GUID, the measuredAt as an autofilled Date and the value as a float
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    sensor = models.ForeignKey(SensorConfig, on_delete=models.DO_NOTHING)
    measuredAt = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
