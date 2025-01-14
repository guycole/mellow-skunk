from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

#router.register(r'heeler', HeelerViewSet)
#router.register(r'heeler', HeelerList)
router.register(r'host', HostViewSet)
router.register(r'hyena', HyenaViewSet)
router.register(r'task', TaskViewSet)
 
# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('heeler/', HeelerList.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]