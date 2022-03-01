from rest_framework import permissions
from django.contrib.auth import get_user_model
User = get_user_model()


class MarkCreatePermission(permissions.BasePermission):
    message = 'Adding marks for non teacher user not allowed.'

    def has_permission(self, request, view):
        if request.user.role != User.TEACHER:
            return False
        return True
