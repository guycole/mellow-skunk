from django.contrib.auth.models import Group, User

from rest_framework import mixins, permissions, status, viewsets
from rest_framework.response import Response

from .apps import HEELER_OBS_GAUGE, POODLE_HUMIDITY_GAUGE, POODLE_PRESSURE_GAUGE, POODLE_TEMPERATURE_GAUGE, POODLE_ORIENTATION_PITCH_GAUGE, POODLE_ORIENTATION_ROLL_GAUGE, POODLE_ORIENTATION_YAW_GAUGE
from .models import Heeler, Poodle
from .serializers import HeelerSerializer, PoodleSerializer, GroupSerializer, UserSerializer

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

class HeelerViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Heeler.objects.all()
    serializer_class = HeelerSerializer
    
    def create(self, request, *args, **kwargs):
        # should always be a list
        is_many = isinstance(request.data, list)
        if is_many:
            heeler_population = float(len(request.data))
            print(f"fresh heeler population: {heeler_population}")
            HEELER_OBS_GAUGE.set(heeler_population) 

            # delete old records
            Heeler.objects.all().delete()

            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PoodleViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Poodle.objects.all()
    serializer_class = PoodleSerializer
    
    def create(self, request, *args, **kwargs):
        POODLE_HUMIDITY_GAUGE.set(request.data['humidity_pct'])
        POODLE_TEMPERATURE_GAUGE.set(request.data['temperature_c'])
        POODLE_PRESSURE_GAUGE.set(request.data['pressure_mb'])
        POODLE_ORIENTATION_PITCH_GAUGE.set(request.data['orientation_pitch_rads'])
        POODLE_ORIENTATION_ROLL_GAUGE.set(request.data['orientation_roll_rads'])
        POODLE_ORIENTATION_YAW_GAUGE.set(request.data['orientation_yaw_rads'])

        # delete old records
        Poodle.objects.all().delete()

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
