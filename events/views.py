from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import EventSeializer
from .models import Event


@api_view(['get'])
def index(request):
    e = Event.objects.all()
    ser = EventSeializer(e, many=True)
    return Response(ser.data)