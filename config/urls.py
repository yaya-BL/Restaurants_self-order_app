
from django.contrib import admin
from django.urls import path, include
from v1.core.views import home

urlpatterns = [
    # Website Urls
    path('', home, name='homepage'),
    # Super Admin Panel Urls
    path('admin/', admin.site.urls),

    # Api Urls
    path('authApis/', include('v1.core.urls')),
    path('itemApis/', include('v1.item.urls')),
    path('cafeApis/', include('v1.shop.urls')),
]
