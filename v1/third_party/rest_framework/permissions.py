from rest_framework.permissions import BasePermission, SAFE_METHODS

class ShopEditDelete(BasePermission):

    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated) and (request.method == 'PATCH' or request.method == 'DELETE')

    def has_object_permission(self, request, view, obj):
        """Object level permission, allow editing self"""
        return self.has_permission(request, view) and request.user == obj.owner
    