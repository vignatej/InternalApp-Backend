from django.urls import re_path
from . import consumers, consumers1
websocket_urlpatterns = [
    re_path(r'oneonechat/(?P<sender_id>\d+)/$', consumers1.chatConsumer.as_asgi()),
    re_path(r'oneonechat/(?P<sender_id>\d+)/(?P<reciever_id>\d+)/$', consumers.ChatConsumer.as_asgi()),
    
]