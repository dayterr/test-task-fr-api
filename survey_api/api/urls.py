from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SurveyViewSet, QuestionViewSet, AnswersViewSet

router_v1 = DefaultRouter()
router_v1.register('answers', AnswersViewSet, basename='participations')
router_v1.register('surveys', SurveyViewSet, basename='surveys')
router_v1.register('questions', QuestionViewSet, basename='questions')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
