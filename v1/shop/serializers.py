from rest_framework import serializers
from django.contrib.auth.models import User
# Model Class imports
from .models import Cafe


class CafeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cafe
    fields = ['name', 'address']
