from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('', views.apiOverview, name="api-overview"),
  # authentication apis
  path('sign-up', views.signUp, name="sign-up"),
  path('sign-in', obtain_auth_token, name="sign-in"),
]