from django.urls import path
from . import consumers

__author__ = 'BENZNANA Mohamed : benznana.med@gmail.com'


websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]