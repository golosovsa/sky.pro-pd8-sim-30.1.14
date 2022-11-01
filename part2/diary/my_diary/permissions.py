from rest_framework import permissions
from my_diary.models import User


# TODO напишите здесь необходимые условия в соответствии с заданием
class MarkCreatePermission(permissions.BasePermission):
    message = 'Adding marks for non teacher user not allowed.'

    def has_permission(self, request, view):
        if request.user.role == User.TEACHER:
            return True
        return False
