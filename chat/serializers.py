from rest_framework import serializers
from .models import Message
from users.serializers import profileSerializer
class MessageSerializer(serializers.ModelSerializer):
    sender = profileSerializer(many=False)
    reciever = profileSerializer(many=False)
    class Meta:
        model = Message
        fields='__all__'
