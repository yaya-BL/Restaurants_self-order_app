# Django imports
from django.shortcuts import render
from django.http import JsonResponse
# DRF imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
# Serializer Class imports
from .serializers import ShopSerializer
# Model Class imports
from django.contrib.auth.models import User
from v1.core.models import Userprofile
from .models import Shop

# APIs for Shop
@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'Shop Create':'/createShop',
    }
  return Response(api_urls)

# create Shop
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def createShop(request):
    if request.method == "POST":
        print(request.user.id)
        serializer = ShopSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save(user=request.user)
            plan = 'seller'
            request.user.userprofile.plan = plan
            request.user.userprofile.save()
            data["success"] = "Congratulations! Now You Upload Items!"
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)