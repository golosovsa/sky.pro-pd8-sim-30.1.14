from rest_framework.generics import CreateAPIView

from django.contrib.auth import get_user_model
from users.serializers import UserCreateSerializer
User = get_user_model()


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
