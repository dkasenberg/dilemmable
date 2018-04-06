from django.db import models
from django.contrib.auth.models import AbstractUser

from dilemmable import settings

# Create your models here.

class DUser(AbstractUser):
    security_question = models.CharField(max_length=100)
    security_answer = models.CharField(max_length=128)
    subscribed = models.BooleanField(default=True)
    last_checked_email = models.DateTimeField(null=True)
    #https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#django.contrib.auth.models.CustomUser.REQUIRED_FIELDS

    def __str__(self):
        return self.username

class PasswordResetRequest(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created = models.DateTimeField(auto_now_add=True)


# class SystemAdmin(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)

# TODO: These should be done with django.contrib.auth views and permissions
# class PasswordResetRequest(models.Model):
#     id = models.CharField(max_length=128, primary_key=True)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL)
#     created = models.DateTimeField(auto_now_add=True)
