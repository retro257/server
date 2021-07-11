from django.db import models

class Question(models.Model):
    author = models.CharField(max_length=255)
    tittle = models.CharField(max_length=255)
    content_text = models.TextField(max_length=255)

class Answer(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField(max_length=255, unique=False)
    question = models.ForeignKey(Question, unique=False, on_delete=models.CASCADE)