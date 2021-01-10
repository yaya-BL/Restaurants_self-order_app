
from django.contrib import admin
from django.urls import path, include
from apps.core.views import home
urlpatterns = [
    # Website Urls
    path('', home, name='homepage'),
    # Super Admin Panel Urls
    path('admin/', admin.site.urls),

    # Api Urls
    path('authApis/', include('apps.core.urls')),
    path('itemApis/', include('apps.item.urls')),
    path('cafeApis/', include('apps.cafe.urls')),
    
]
