from questions.models import Question, Answers
from rest_framework import serializers
from django.conf import settings


class QuestionSerializer(serializers.ModelSerializer):
    author_id = serializers.SerializerMethodField(read_only=True)
    answers = serializers.StringRelatedField(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    user_has_answered = serializers.SerializerMethodField(read_only=True)
    user_has_upvoted = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Question
        exclude = ["updated_at", "voters"]
######

    def get_created_at(self, instance):
        return instance.created_at

    def get_answers_count(self, instance):
        return instance.answers.count()

    def get_user_has_answered(self, instance):
        request = self.context["request"]
        if request.user.is_anonymous:
            return "anonymous user"
        return instance.answers.filter(author=request.user).exists()

    def get_user_has_upvoted(self, instance):
        request = self.context["request"]
        return instance.voters.filter(pk=request.user.pk).exists()

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_author_id(self,instance):
        return instance.author.ID

######


class AnswerSerializer(serializers.ModelSerializer):
    author_id = serializers.SerializerMethodField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    user_has_upvoted = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Answers
        exclude = ["voters", "updated_at", "question"]
###

    def get_created_at(self, instance):
        return instance.created_at

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_upvoted(self, instance):
        request = self.context["request"]
        return instance.voters.filter(pk=request.user.pk).exists()

    def get_author_id(self,instance):
        return instance.author.ID

 

 