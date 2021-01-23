from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Shop

class ShopEditDelete(BasePermission):

    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated) and \
            (request.method == 'PATCH' or request.method == 'DELETE')

    def has_object_permission(self, request, view, obj):
        """Object level permission, allow editing self"""
        return self.has_permission(request, view) and request.user == obj.owner

class ShopBranchCreate(BasePermission):

    def has_permission(self, request, view):
        flag = False
        if Shop.objects.get(id=request.data['shop']).owner == request.user:
            flag = True
        print(request.data['shop'])
        return (request.user and request.user.is_authenticated) and flag

    def has_object_permission(self, request, view, obj):
        """Object level permission, allow editing self"""
        return self.has_permission(request, view)
    