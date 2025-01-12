# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import Heeler
 
# Create a model serializer
class HeelerSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Heeler
        fields = ('essid', 'address')
