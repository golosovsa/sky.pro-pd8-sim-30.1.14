from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "user"):
            return request.user and request.user.is_authenticated and obj.user == request.user
        else:
            return request.user and request.user.is_authenticated and obj.user == request.user
