
import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthenticationMiddleware
import app.routing

application = ProtocolTypeRouter({
    'websocket':AuthenticationMiddleware(
        URLRouter(
            app.routing.websocket_urlpatterns
        )
    )
  
}) 