# DRF imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework import mixins

# Serializer Class imports
from .serializers import ShopSerializer
from .models import Shop

from rest_framework.viewsets import GenericViewSet

# APIs for Shop
@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'Shop Create':'/createShop',
    }
  return Response(api_urls)
'''
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
            #request.user.userprofile.plan = plan
            #request.user.userprofile.save()
            data["success"] = "Congratulations! Now You Upload Items!"
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''

#create Shop
class ShopCreateAPIView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
  serializer_class = ShopSerializer
  queryset = Shop.objects.all()

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
  
  permission_classes = [IsAuthenticated]
