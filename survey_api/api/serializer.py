from rest_framework import serializers

from .models import Survey, Question, UserAnswer


class UserAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAnswer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=Question.QUESTION_TYPES)

    class Meta:
        model = Question
        fields = ('text', 'type')


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ('title', 'questions')





