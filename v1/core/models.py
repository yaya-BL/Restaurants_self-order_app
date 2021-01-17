from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserType(models.Model):
  name = models.CharField(max_length=20)
  def __str__(self):
    return self.name

class UserProfile(models.Model):
  user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
  user_type = models.ForeignKey(UserType, related_name="userprofile", blank=True, null=True, on_delete=models.CASCADE)
  country = models.CharField(max_length=20, blank=True, null=True)

  def __str__(self):
    return self.user.email