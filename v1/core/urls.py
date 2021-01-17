from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('', views.apiOverview, name="api-overview"),
  # authentication apis
  path('register', views.signUp, name="sign-up"),
  path('login', obtain_auth_token, name="sign-in"),
]