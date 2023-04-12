from django.urls import path
from .views import chatter_random, getAllPrevMessagesAndUsers

urlpatterns = [
    path('room/', getAllPrevMessagesAndUsers, name='course_chat_room'),

]