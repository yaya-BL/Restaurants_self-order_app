from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Cafe(models.Model):
  user = models.OneToOneField(User, related_name='cafe', on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  address = models.TextField(blank=True, null=True)

  class Meta:
    verbose_name_plural='Cafe'
    
  def __str__(self):
    return self.name