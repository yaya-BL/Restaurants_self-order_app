
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

#from v1.shop.urls import router as shop_router
'''
urlpatterns = [
    # Website Urls
    path('', home, name='homepage'),
    # Super Admin Panel Urls
    path('admin/', admin.site.urls),

    # Api Urls
    path('v1/auth/', include('v1.core.urls')),
    path('v1/', include('v1.item.urls')),
    path('v1/shop/', include('v1.shop.urls')),
    path('auth/', include('djoser.urls')),
    #path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('shop/', include('v1.shop.urls'))
]

router = DefaultRouter(trailing_slash=False)

urlpatterns += router.urls
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)