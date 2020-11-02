from django.db import models
from django.conf import settings


class Question(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    content = models.CharField(max_length=500)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE, related_name="questions")
    voters = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="q_voters")

    def __str__(self):
        return self.content


class Answers(models.Model):

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    body = models.TextField()
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE, related_name="answers")
    voters = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="a_voters")

    def __str__(self):
        return f"{self.author.username} : {self.body}"
