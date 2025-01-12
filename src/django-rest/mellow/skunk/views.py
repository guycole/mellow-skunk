from django.shortcuts import render
from rest_framework import permissions, viewsets
from django.contrib.auth.models import Group, User
 
from .serializers import HeelerSerializer, HostSerializer, HyenaSerializer, TaskSerializer, GroupSerializer, UserSerializer
from .models import Heeler, Host, Hyena, Task

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
 
class HeelerViewSet(viewsets.ModelViewSet):
    queryset = Heeler.objects.all()
    serializer_class = HeelerSerializer

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

class HyenaViewSet(viewsets.ModelViewSet):
    queryset = Hyena.objects.all()
    serializer_class = HyenaSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
