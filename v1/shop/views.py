# DRF imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework import mixins

# Serializer Class imports
from .serializers import ShopSerializer, ShopBranchSerializer
from .models import Shop

from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from .permissions import ShopEditDelete, ShopBranchCreate

#create Shop
class ShopCreateAPIView(CreateAPIView, GenericAPIView):
  serializer_class = ShopSerializer

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

  permission_classes = [IsAuthenticated]

#edit the Shop
#only owner of the shop can edit the shop
class ShopEditAPIView(UpdateAPIView, GenericAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [ShopEditDelete]

#delete the shop
#only owner of the shop can delete shop
class ShopDeleteAPIView(DestroyAPIView, GenericAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [ShopEditDelete]
  
class BranchCreateAPIView(CreateAPIView, GenericAPIView):
  serializer_class = ShopBranchSerializer
  permission_classes = [ShopBranchCreate]