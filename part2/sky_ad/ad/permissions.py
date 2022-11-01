from rest_framework import permissions


# TODO напишите здесь необходимые условия в соответствии с заданием
class AdUpdatePermission(permissions.BasePermission):
    message = 'Updating not your add is not permitted'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
