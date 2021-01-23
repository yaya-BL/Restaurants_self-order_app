from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class BranchType(models.Model):
  name = models.CharField(max_length=16)

  def __str__(self):
    return self.name

class Shop(models.Model):
  name = models.CharField(max_length=255)
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='uploads/shop/', blank=True, null=True)

  def __str__(self):
    return self.name

class Country(models.Model):
  name = models.CharField(max_length = 255)
  alpha_two_code = models.CharField(max_length = 2, blank=True, null=True)

  def __str__(self):
      return self.name
  
class ShopBranch(models.Model):
  shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
  branch_type = models.ForeignKey(BranchType, on_delete=models.DO_NOTHING)
  location = models.CharField(max_length=255, blank=True, null=True)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=255, blank=True, null=True)
  country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
  description = models.TextField()
  opening_time = models.TimeField()
  closing_time = models.TimeField()

def __str__(self):
    return self.shop.name

# model to handle the relationship between a User and
# a particular branch for authorization
class UserBranch(models.Model):
  PermChoices = [
        (0, 'Read'),
        (1, 'Create'),
        (2, 'Update'),
        (3, 'Delete')
    ]
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  branch = models.ForeignKey(ShopBranch, on_delete=models.CASCADE)
  perm = models.IntegerField(choices=PermChoices, default=0)

  def __str__(self):
    return self.branch.name + ", " + self.user.email + ": " + str(self.perm)

  class Meta:
    unique_together = ['user', 'branch']