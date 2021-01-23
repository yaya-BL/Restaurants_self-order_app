from .views import ShopCreateAPIView
from rest_framework.routers import SimpleRouter

'''
urlpatterns = [
  path('', views.apiOverview, name="api-overview"),
  # authentication apis
  path('add', views.createShop, name="createCafe"),
]
'''
router = SimpleRouter(trailing_slash=False)
router.register('shop', ShopCreateAPIView, basename='shop-create')
