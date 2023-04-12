from django.urls import path
from .views import allClasses, addClassRoom, addPost, getPosts, getBucket, getClass, changeDescription
urlpatterns = [
    path("getAllClasses",allClasses, name="get all classrooms"),
    path("addClassroom",addClassRoom, name="add a classroom"),
    path("addPost",addPost, name="add a new post"),
    path("getPosts",getPosts, name="get all posts from a classroom"),
    path("getBucket", getBucket, name="get all bucket items from the classroom"),   
    path("getAClass", getClass, name="get a specific class"),   
    path('changeDescription',changeDescription, name="to change desc of a class")
]