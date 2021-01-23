from .views import ShopCreateAPIView, ShopEditAPIView, ShopDeleteAPIView, BranchCreateAPIView, BranchUpdateAPIView
from rest_framework.routers import SimpleRouter
from django.urls import path

urlpatterns = [
  path('add/', ShopCreateAPIView.as_view(), name="create-shop"),
  path('<str:pk>/edit/', ShopEditAPIView.as_view(), name="edit-shop"),
  path('<str:pk>/delete/', ShopDeleteAPIView.as_view(), name="delete-shop"),
  path('branch/add/', BranchCreateAPIView.as_view(), name="create-branch"),
  path('branch/<str:pk>/edit/', BranchUpdateAPIView.as_view(), name="edit-branch"),
]