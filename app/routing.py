from django.urls import path
from . import consumers


websocket_urlpatters = [
    path('ws/sc/', consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/', consumers.MyAsyncConsumer.as_asgi()),
    path('ws/chat/', consumers.MyChatConsumer.as_asgi())
]