from django.contrib import admin
from .models import *


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name','host')

@admin.register(Message)
class MsgAdmin(admin.ModelAdmin):
    list_display = ('room','user','text')