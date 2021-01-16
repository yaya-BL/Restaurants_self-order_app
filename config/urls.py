
from django.contrib import admin
from django.urls import path, include
from v1.core.views import home

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
