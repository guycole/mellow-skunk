import datetime
#import pytz
import uuid

from django.db import models

class Heeler(models.Model):
    bssid = models.CharField(max_length=32)
    ssid = models.CharField(max_length=32)
    frequency_mhz = models.IntegerField(default=-1)
    time_stamp_z = models.DateTimeField(auto_now_add=False)

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
    latitude_decdeg = models.FloatField(default=0.0)
    longitude_decdeg = models.FloatField(default=0.0)
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

class Poodle(models.Model):
    humidity_pct = models.FloatField(default=-1.0)
    temperature_c = models.FloatField(default=-1.0)
    pressure_mb = models.FloatField(default=-1.0)
    orientation_pitch_rads = models.FloatField(default=-1.0)
    orientation_roll_rads = models.FloatField(default=-1.0)
    orientation_yaw_rads = models.FloatField(default=-1.0)
    time_stamp_z = models.DateTimeField(auto_now_add=False)

    class Meta:
        ordering = ("time_stamp_z",)

    def __repr__(self):
        return self.time_stamp_z

    def __str__(self):
        return self.time_stamp_z

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
