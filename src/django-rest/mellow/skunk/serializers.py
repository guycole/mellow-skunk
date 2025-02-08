# import serializer from rest_framework
from rest_framework import serializers
 
from .models import Heeler, Host, Hyena, Poodle, Task

from django.contrib.auth.models import Group, User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class HeelerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Heeler
        fields = ('bssid', 'ssid', 'frequency_mhz', 'time_stamp_z')

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ('active_flag', 'location', 'host', 'latitude_decdeg', 'longitude_decdeg', 'type')

class HyenaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hyena
        fields = ('flight', 'hex', 'time_stamp')

class PoodleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poodle
        fields = ('humidity_pct', 'temperature_c', 'pressure_mb', 'orientation_pitch_rads', 'orientation_roll_rads', 'orientation_yaw_rads', 'time_stamp_z')

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'active_flag', 'name')
    
# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
