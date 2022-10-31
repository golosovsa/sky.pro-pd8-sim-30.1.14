from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

from register.serializers import UserCreateSerializer

User = get_user_model()


# TODO опишите view для создания пользователя ниже
class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
