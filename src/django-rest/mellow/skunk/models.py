import datetime
#import pytz
import uuid

from django.db import models

# update
class Heeler(models.Model):
    bssid = models.CharField(max_length=32)
    ssid = models.CharField(max_length=32)
    frequency = models.CharField(max_length=32)
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("ssid",)

    def __repr__(self):
        return self.ssid

    def __str__(self):
        return self.ssid

class Host(models.Model):
    active_flag = models.BooleanField(default=False)
    location = models.CharField(max_length=32)
    host = models.CharField(max_length=32)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    type = models.CharField(max_length=32)

    class Meta:
        ordering = ("host",)

    def __repr__(self):
        return self.host

    def __str__(self):
        return self.host

class Hyena(models.Model):
    flight = models.CharField(max_length=32)
    hex = models.CharField(max_length=32)
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("hex",)

    def __repr__(self):
        return self.hex

    def __str__(self):
        return self.hex

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    active_flag = models.BooleanField(default=False)
    name = models.CharField(max_length=32)

    class Meta:
        ordering = ("name",)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
    
# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
