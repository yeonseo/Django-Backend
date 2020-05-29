from django.urls import path
from . import views
from rooms import views as room_views
from django.conf import  settings
from rest_framework import routers

app_name = "core"

urlpatterns = [path("", room_views.HomeView.as_view(), name="home")]