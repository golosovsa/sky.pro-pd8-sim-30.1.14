from rest_framework import serializers

from django.contrib.auth import get_user_model

from register.models import User


# TODO опишите сериалайзер для создания пользователя ниже
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(validated_data["password"])
        user.save()

        return user
