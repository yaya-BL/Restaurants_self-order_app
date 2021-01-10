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
from .serializers import CafeSerializer
# Model Class imports
from django.contrib.auth.models import User
from apps.core.models import Userprofile
from .models import Cafe

# APIs for Cafe
@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'Cafe Create':'/createCafe',
    }
  return Response(api_urls)

# createCafe
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def createCafe(request):
    if request.method == "POST":
        user = request.user
        print(user.id)
        cafe = Cafe(user = user)
        serializer = CafeSerializer(cafe, data=request.data)
        data={}
        if serializer.is_valid():
            cafe = serializer.save()
            plan = 'seller'
            user.userprofile.plan = plan
            user.userprofile.save()
            data["success"] = "Congratulations! Now You Upload Items!"
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def createCafe(request):
#     if request.method == "POST":
#         serializer = CafeSerializer(data=request.data)
#         data={}
#         if serializer.is_valid():
#             cafe = serializer.save()
#             serializer.save(owner=request.user)
#             userId = cafe.user.id
#             user = User.objects.filter(id=userId).get()
#             print(user.id)
#             plan = 'seller'
#             user.userprofile.plan = plan
#             user.userprofile.save()
#             data["success"] = "Congratulations! Now You Upload Items!"
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
