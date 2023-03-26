
import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import  AuthMiddlewareStack
import app.routing

from app.middleware import JwtAuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatApp.settings')
django.setup()
application = ProtocolTypeRouter({
    'http':get_asgi_application(), 
    'websocket': JwtAuthMiddlewareStack(
        URLRouter(
            app.routing.websocket_urlpatterns
        )
    )
  
}) 