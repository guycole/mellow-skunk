from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'heeler', HeelerViewSet, basename='heeler')

#router.register(r'users', UserViewSet)
#router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
