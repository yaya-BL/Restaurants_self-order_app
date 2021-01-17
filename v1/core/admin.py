from django.contrib import admin

from .models import UserProfile, UserType

admin.site.register(UserType)
admin.site.register(UserProfile)
