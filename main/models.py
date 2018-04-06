from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dilemma(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)
    text = models.TextField()

class DilemmaOption(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    dilemma = models.ForeignKey('Dilemma')
    text = models.CharField(max_length = 1000)

class DilemmaChoice(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    dilemma_option =models.ForeignKey('DilemmaOption')
    user = models.ForeignKey(User)