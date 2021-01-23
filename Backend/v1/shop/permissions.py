from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Shop, UserBranch, ShopBranch

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
        return (request.user and request.user.is_authenticated) and flag

    def has_object_permission(self, request, view, obj):
        """Object level permission, allow editing self"""
        return self.has_permission(request, view)
    
class ShopBranchUpdate(BasePermission):

    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        """Object level permission, allow editing self"""
        flag = False
        if UserBranch.objects.filter(user=request.user, branch=obj).exists():
            perm = UserBranch.objects.get(user=request.user, branch=obj).perm
            if perm == 1 or perm == 2 or perm == 3:
                flag = True
        if Shop.objects.filter(shopbranch=obj, owner= request.user).exists():
            flag = True
        return self.has_permission(request, view) and flag
    