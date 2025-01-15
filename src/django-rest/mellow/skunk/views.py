from django.shortcuts import render
from rest_framework import generics, mixins, permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import Group, User
 
from .serializers import HeelerSerializer, HostSerializer, HyenaSerializer, TaskSerializer, GroupSerializer, UserSerializer
from .models import Heeler, Host, Hyena, Task
from .apps import HEELER_OBS_GAUGE

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

class HeelerList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    List all heeler observations, or create fresh observations.
    """
    serializer_class = HeelerSerializer
    
    def get(self, request, format=None):
        selected = Heeler.objects.all()
        serializer = HeelerSerializer(selected, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        if is_many:
            HEELER_OBS_GAUGE.set(len(request.data)) 
            Heeler.objects.all().delete() # delete old
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#class HeelerViewSet(viewsets.ModelViewSet):
#    queryset = Heeler.objects.all()
#    serializer_class = HeelerSerializer

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

class HyenaViewSet(viewsets.ModelViewSet):
    queryset = Hyena.objects.all()
    serializer_class = HyenaSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
