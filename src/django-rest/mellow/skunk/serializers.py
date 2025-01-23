# import serializer from rest_framework
from rest_framework import serializers
 
from .models import Heeler, Host, Hyena, Task

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
        fields = ('bssid', 'ssid', 'frequency', 'time_stamp')

class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('active_flag', 'location', 'host', 'latitude', 'longitude', 'type')

class HyenaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hyena
        fields = ('flight', 'hex', 'time_stamp')

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'active_flag', 'name')
    
# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
