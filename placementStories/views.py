from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import story, question, answer
from .serializers import storiesSerializer, storySerializer
@api_view(['GET'])
def getStories(request):
    stories = story.objects.all()
    serializer = storiesSerializer(stories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStory(request, pk):
    stor = story.objects.get(id=pk)
    serializer = storySerializer(stor, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addStories(request):
    print(request.data)
    if request.data.get('story',-1)==-1:
        return Response('please Add Story')
    newStory = story.objects.create(
        Text = request.data['story'],
        user=request.user.profile
    )
    newStory.save()
    return Response('ok!hhh')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addQuestions(request):
    data = request.data
    print(data)
    q=dict(data)
    print(q)
    stor = story.objects.get(id = int(q['id'][0]))
    if (stor.user.user == request.user):
        return Response('saavu')
    ques = question.objects.create(
        user = request.user.profile,
        story= stor,
        Text = q['question'][0]
    )
    ques.save()
    print(ques.id)
    return Response('ok addd a new ques') 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addAnswer(request):
    data=request.data
    print(data)
    ques = question.objects.get(pk = int(data['id']))
    ans = answer.objects.create(
        user=request.user.profile,
        question=ques,
        Text = data['answer']
    )
    ans.save()
    return Response('Answer added sucessfully')


