from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import ClassRoom, Posts, BucketItems
from .serializers import ClassRoomSerializer, BucketItemsSerializer, PostsSerializer

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allClasses(request):
    classes = ClassRoom.objects.all()
    ser = ClassRoomSerializer(classes, many=True)
    return Response(ser.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getClass(request):
    clas = ClassRoom.objects.get(id=request.data["classID"])
    ser = ClassRoomSerializer(clas, many=False)
    return Response(ser.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addClassRoom(request):
    newclass = ClassRoom.objects.create(
        name=request.data["name"],
        code=request.data['code'],
        year = int(request.data['year']),
        sem = request.data['sem'],
        teacher_name = request.data['teacher_name'],
        description = request.data["description"],
        created_by = request.user.profile
    )
    newclass.save()
    ser = ClassRoomSerializer(newclass, many=False)
    return Response(ser.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def changeDescription(request):
    clas = ClassRoom.objects.get(id=int(request.data["classId"]))
    clas.description = request.data["description"]
    clas.save()
    return Response("success")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addPost(request):
    cls = ClassRoom.objects.get(id = int(request.data['classId']))
    newPost = Posts.objects.create(
        classRoom = cls,
        description = request.data["description"],
        created_by = request.user.profile
    )
    newPost.save()
    if(request.FILES):
        fil = request.FILES.keys()
        print(fil)
        for i in request.FILES.keys():
            newBuc = BucketItems(
                file = request.FILES[i],
                post = newPost,
                created_by = request.user.profile
            )
            print("ho ho")
            newBuc.save()
    return Response("success")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getPosts(request):
    print(request.data['classId'])
    cls = ClassRoom.objects.get(id = int(request.data['classId']))
    psts = cls.posts_set.all()
    ser = PostsSerializer(psts, many=True)
    return Response(ser.data[::-1])

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getBucket(request):
    cls = ClassRoom.objects.get(id = int(request.data['classId']))
    posts = Posts.objects.filter(classRoom = cls)
    bucketitems = BucketItems.objects.filter(post__in=posts)
    ser = BucketItemsSerializer(bucketitems, many=True)
    return Response(ser.data)
