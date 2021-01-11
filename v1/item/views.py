# Django imports
from django.shortcuts import render
from django.http import JsonResponse
# DRF imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
# Serializer Class imports
from .serializers import CategorySerializer, ItemSerializer
# Model Class imports
from .models import Category, Item
from v1.shop.models import Cafe

# APIs for category and Item
@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'Category List':'/category-list',
    'Category Detail View':'/category-detail/<str:pk>',
    'Category Create':'/category-create',
    'Category Update':'/category-update/<str:pk>',
    'Category Delete':'/category-delete/<str:pk>',

    'ItemList':'/item-list',
    'Item Detail View':'/item-detail/<str:pk>',
    'Item Create':'/item-create',
    'Item Update':'/item-update/<str:pk>',
    'Item Delete':'/item-delete/<str:pk>',
    }
  return Response(api_urls)

# methods for category 
# categoryList
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def categoryList(request):
  categories = Category.objects.all().order_by('-id')
  serializer = CategorySerializer(categories, many=True)
  return Response(serializer.data)

# categoryDetail
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def categoryDetail(request, pk):
  category = Category.objects.get(id=pk)
  serializer = CategorySerializer(category, many=False)
  return Response(serializer.data)

# categoryCreate
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def categoryCreate(request):
  user = request.user
  user_id = Category(user = user)
  cafe = request.user.cafe
  cafe_id = Category(cafe = cafe)
  # cafe = Cafe.objects.filter(user_id=user.id).get()
  # cafe_id = Category(cafe = cafe)
  print(cafe)
  # context = {'user_id': user_id, 'cafe_id': cafe_id}
  serializer = CategorySerializer(data = {'user_id': user_id, 'cafe_id': cafe_id})
  data={}
  if serializer.is_valid():
    serializer.save()
    data["success"] = "Category Has Been Created!"
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# categoryUpdate
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def categoryUpdate(request, pk):
  category = Category.objects.get(id=pk)
  user = request.user
  if category.created_by != user:
    return Response({'Response':"You dont have Permission to edit this data."})
  serializer = CategorySerializer(instance=category, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

# categoryDelete
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def categoryDelete(request, pk):
  category = Category.objects.get(id=pk)
  user = request.user
  if category.created_by != user:
    return Response({'Response':"You dont have Permission to delete this data."})
  category.delete()
  return Response('Category succsesfully delete!')

# methods for Items
@api_view(['GET'])
def itemList(request):
  try:
    items = Item.objects.all().order_by('-id')
  except Item.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == "GET":
    serializer = ItemSerializer(items, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def itemDetail(request, pk):
  try:
    item = Item.objects.get(id=pk)
  except Item.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = ItemSerializer(item, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def itemCreate(request):
  if request.method == "POST":
    serializer = ItemSerializer(data=request.data)
    data={}
    if serializer.is_valid():
      serializer.save()
      data["success"]="Create Successful"
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def itemUpdate(request, pk):
  try:
    item = Item.objects.get(id=pk)
  except Item.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == "POST":
    serializer = ItemSerializer(instance=item, data=request.data)
    data={}
    if serializer.is_valid():
      serializer.save()
      data["success"]="update Successful"
      return Response (data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def itemDelete(request, pk):
  try:
    item = Item.objects.get(id=pk)
  except Item.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "DELETE":
    operation = item.delete()
    data={}
    if operation:
      data["success"]="Delete Successful"
    else:
      data["failure"]="Delete Failed"
    return Response(data=data)

