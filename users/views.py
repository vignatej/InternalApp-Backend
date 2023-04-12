from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from .models import profile
from .serializers import profileSerializer


@api_view(['POST'])
def createUser(request):
    data=request.data
    try:
        user=User.objects.create(
            username=data['username'],
            email=data['email'],
        )
        user.set_password(data['password'])
        user.save()
    except:
        return Response('there is already a user with same email or password')
    try:
        prof=profile.objects.create(
            user=user,
            name=user.username,
            email = user.email,
            branch = data['branch'],
            startYear = data['startYear'],
            tagline = data['tagline'],
            profilePhoto=request.FILES['image']
        )
        prof.save()
    except:
        user.delete()
        return Response('please enter all inputs and profile pic')
    
    return Response('sucessfully created yout account')

@api_view(['get'])
@permission_classes([IsAuthenticated])
def getUserDeatils(request):
    prof = request.user.profile
    serializer = profileSerializer(prof, many=False)
    return Response(serializer.data)


@api_view(['get'])
def getProfiles(request):
    prof = profile.objects.all()
    ser = profileSerializer(prof, many=True)
    return Response(ser.data)