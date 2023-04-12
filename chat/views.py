from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Message
from django.db.models import Q
from .serializers import MessageSerializer
from users.models import profile
from users.serializers import profileSerializer
# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def chatter_random(request):
    return Response("vacchindha")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllPrevMessagesAndUsers(request):
    msg = Message.objects.filter(Q(sender=request.user.profile)|Q(reciever = request.user.profile))
    messages = MessageSerializer(msg, many=True)
    mes = list(messages.data)
    mes.sort(key=lambda x:x['id'], reverse=True)
    users = []
    for i in mes:
        if i['sender'] not in users:
            users.append(i['sender'])
        if i['reciever'] not in users:
            users.append(i['reciever'])
    prof = profile.objects.all()
    seria = profileSerializer(prof, many=True)
    profilesAll = list(seria.data)
    for i in profilesAll:
        if i not in users:
            users.append(i)
    return Response([mes, users])