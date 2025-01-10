import datetime
#import pytz
import uuid

from django.db import models

class Heeler(models.Model):
    address = models.CharField(max_length=32)
    essid = models.CharField(max_length=32)
    frequency = models.CharField(max_length=32)
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("essid",)

    def __repr__(self):
        return self.essid

    def __str__(self):
        return self.essid

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

#class Observation(models.Model):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#    host = models.ForeignKey(Host, on_delete=models.CASCADE)
#    timestamp = models.DateTimeField(default=datetime.datetime.now(pytz.utc))
#
#    class Meta:
#        ordering = ("timestamp",)
#
#    def __repr__(self):
#        return f"{self.host} at {self.timestamp}"
#
#    def __str__(self):
#        return f"{self.host} at {self.timestamp}"
#
#class Sample(models.Model):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#    observation = models.ForeignKey(Observation, on_delete=models.CASCADE)
#    name = models.CharField(max_length=32)
#    value = models.FloatField()
#
#      id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#    created = models.DateTimeField(auto_now_add=True)
#    modified = models.DateTimeField(auto_now_add=True)
#
#    class Meta:
#        ordering = ("observation", "name")
#
#    def __repr__(self):
#        return f"{self.name} = {self.value}"
#
#    def __str__(self):
#        return f"{self.name} = {self.value}"
    
# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
