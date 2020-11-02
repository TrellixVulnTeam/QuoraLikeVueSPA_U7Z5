from django.urls import path, include
from .views import (QuestionViewSet,
                    AnswerCreateApiView, AnswerListApiView, AnswerRetrieveUpdateDestroy,
                    ToggleAnswerVoters, ToggleQuestionVoters)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)


app_name = "questions"

urlpatterns = [
    path("", include(router.urls)),
    path("answer_create/<slug:slug>/",
         AnswerCreateApiView.as_view(), name="create-answer"),
    path("answers_list/<slug:slug>/",
         AnswerListApiView.as_view(), name="list-answers"),
    path("answers/<int:pk>/", AnswerRetrieveUpdateDestroy.as_view(),
         name="answer-detail"),
    path("toggle_a_voters/<int:pk>/",
         ToggleAnswerVoters.as_view(), name="toggle-answer-voters"),
    path("toggle_q_voters/<slug:slug>/",
         ToggleQuestionVoters.as_view(), name="toggle-question-voters"),
]
