from questions.models import Question, Answers
from .serializers import QuestionSerializer, AnswerSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.validators import ValidationError
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from .custom_permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status


class QuestionViewSet(ModelViewSet):

    queryset = Question.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = QuestionSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnswerCreateApiView(generics.CreateAPIView):

    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        kwargs_slug = self.kwargs["slug"]
        question = get_object_or_404(Question, slug=kwargs_slug)

        if Answers.objects.filter(question__slug=kwargs_slug, author=self.request.user).exists():
            raise ValidationError(
                "You can't respond to a question more than once, please delete your preview answer or update it")

        serializer.save(question=question, author=self.request.user)


class AnswerListApiView(generics.ListAPIView):

    serializer_class = AnswerSerializer

    def get_queryset(self):
        kwargs_slug = self.kwargs["slug"]
        queryset = Answers.objects.filter(
            question__slug=kwargs_slug).order_by("-created_at")

        return queryset


class AnswerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ToggleAnswerVoters(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        answer_object = get_object_or_404(Answers, pk=pk)
        user = request.user
        if not user in answer_object.voters.all():
            answer_object.voters.add(user)
        else:
            answer_object.voters.remove(user)

        serializer_context = {"request": request}
        serializer = AnswerSerializer(
            answer_object, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ToggleQuestionVoters(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        kwargs_slug = self.kwargs["slug"]
        question_object = get_object_or_404(Question, slug=kwargs_slug)
        user = request.user

        if not user in question_object.voters.all():
            question_object.voters.add(user)
        else:
            question_object.voters.remove(user)

        serializer_context = {"request": request}
        serializer = QuestionSerializer(
            question_object, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
