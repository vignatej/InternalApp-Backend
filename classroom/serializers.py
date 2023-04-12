from rest_framework import serializers
from .models import ClassRoom, BucketItems,Posts
from users.serializers import profileSerializer

class ClassRoomSerializer(serializers.ModelSerializer):
    created_by = profileSerializer(many=False)
    class Meta:
        model = ClassRoom
        fields="__all__"

class BucketItemsSerializer(serializers.ModelSerializer):
    created_by = profileSerializer(many=False)
    class Meta:
        model = BucketItems
        fields="__all__"

class PostsSerializer(serializers.ModelSerializer):
    created_by = profileSerializer(many=False)
    files = serializers.SerializerMethodField()
    class Meta:
        model=Posts
        fields="__all__"
    def get_files(self, obj):
        fil = obj.bucketitems_set.all()
        serializer = BucketItemsSerializer(fil, many=True)
        return serializer.data
    
class clsSer(serializers.ModelSerializer):
    posts = PostsSerializer(many=True)
    # bucket = BucketItemsSerializer(many=True)
    class Meta:
        model = ClassRoom
        fields = "__all__"
    def get_posts(self, obj):
        pos = obj.posts_set.all()
        serializer = PostsSerializer(pos, many=True)
        return serializer.data
       
