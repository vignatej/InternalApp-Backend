from rest_framework import serializers
from .models import story, question, answer
from users.serializers import profileSerializer

class answerSerializer(serializers.ModelSerializer):
    user = profileSerializer(many = False)
    class Meta:
        model = answer
        fields='__all__'


class questionSerializer(serializers.ModelSerializer):
    user=profileSerializer(many = False)
    answers = serializers.SerializerMethodField()
    class Meta:
        model = question
        fields='__all__'
    def get_answers(self, obj):
        ans = obj.answer_set.all()
        serializer = answerSerializer(ans, many=True)
        return serializer.data

class storiesSerializer(serializers.ModelSerializer):
    user=profileSerializer(many = False)
    # questions=serializers.SerializerMethodField()
    class Meta:
        model = story
        fields='__all__'
    # def get_questions(self, obj):
    #     ques = obj.question_set.all()
    #     serializer = questionSerializer(ques, many=True)
    #     return serializer.data

class storySerializer(serializers.ModelSerializer):
    user=profileSerializer(many = False)
    questions=serializers.SerializerMethodField()
    class Meta:
        model = story
        fields='__all__'
    def get_questions(self, obj):
        ques = obj.question_set.all()
        serializer = questionSerializer(ques, many=True)
        return serializer.data

