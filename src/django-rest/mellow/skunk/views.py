from django.shortcuts import render

# Create your views here.
# import viewsets
from rest_framework import viewsets
 
# import local data
from .serializers import HeelerSerializer
from .models import Heeler
 
# create a viewset
 
class HeelerViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Heeler.objects.all()
 
    # specify serializer to be used
    serializer_class = HeelerSerializer
