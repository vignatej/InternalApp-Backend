from django.urls import path
from .views import getStories,addStories, getStory, addQuestions, addAnswer
urlpatterns = [
    path('story/<str:pk>', getStory, name="getStory"),
    path('',getStories,name='getAllStories'),
    path('addStory',addStories, name='patahdhi'),
    path('addQuestion', addQuestions, name="addAQuestion"),
    path('addAnswer', addAnswer, name="addAnswer")
]