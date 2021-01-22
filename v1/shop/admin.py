from django.contrib import admin

from .models import Shop, BranchType, ShopBranch, Country

admin.site.register(Shop)
admin.site.register(BranchType)
admin.site.register(ShopBranch)
admin.site.register(Country)

