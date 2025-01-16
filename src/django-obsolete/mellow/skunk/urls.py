from django.urls import path

from . import views

app_name = "skunk"

urlpatterns = [
    path("", views.index, name="index"),
    path("heeler/", views.HeelerView.as_view(), name="heeler"),
    path("hyena/", views.HyenaView.as_view(), name="hyena"),
]