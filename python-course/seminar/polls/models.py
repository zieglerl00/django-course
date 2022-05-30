from django.db import models


# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=300)
    date = models.DateTimeField()


class Choice(models.Model):
    question = models.ForeignKey(Question, models.CASCADE)
    text = models.CharField(max_length=300)
    count = models.IntegerField(default=0)
