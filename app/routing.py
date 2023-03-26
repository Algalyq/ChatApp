from django.urls import re_path, path
from .consumers import  *

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
    path("ws/", UserConsumer.as_asgi()),
    path('ws/chat2/', RoomConsumer.as_asgi()),
]