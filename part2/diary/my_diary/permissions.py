from rest_framework import permissions


# TODO напишите здесь необходимые условия в соответствии с заданием
class MarkCreatePermission(permissions.BasePermission):
    message = 'Adding marks for non teacher user not allowed.'
