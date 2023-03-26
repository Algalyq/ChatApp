
from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    # path('', index,name="index"),
    path('<str:room_name>/',room,name="room"),
    path('room/<int:pk>/', room2, name='room'),
    path('', index, name='index'),
]
