from rest_framework import viewsets, decorators, response

from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny

from .serializer import SurveySerializer, QuestionSerializer, UserAnswerSerializer
from .models import Survey, Question, UserAnswer
from .permissions import IsAdminOrReadOnly


class SurveyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswersViewSet(viewsets.GenericViewSet,
                           CreateModelMixin, ListModelMixin, RetrieveModelMixin):
    permission_classes = (AllowAny,)
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer


