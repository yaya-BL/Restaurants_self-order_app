from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Shop(models.Model):
  CAFE ='cafe'
  RESTAURANT = 'restaurant'

  CHOICES_TYPES = (
    (CAFE, 'cafe'),
    (RESTAURANT, 'restaurant')
  )

  
  name = models.CharField(max_length=255)
  user = models.OneToOneField(User, related_name='shop',blank=True, null=True, on_delete=models.CASCADE)
  address = models.TextField(blank=True, null=True)
  types = models.CharField(max_length=20, choices=CHOICES_TYPES, default=CAFE)

  class Meta:
    verbose_name_plural='Shop'
    
  def __str__(self):
    return self.name