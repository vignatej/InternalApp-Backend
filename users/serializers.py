from rest_framework import serializers
from .models import profile

class profileSerializer(serializers.ModelSerializer):
    profilePhoto = serializers.ImageField(required=False)
    class Meta:
        model = profile
        fields='__all__'
    