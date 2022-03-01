from django.contrib.auth import get_user_model
from rest_framework import serializers
from my_diary.models import Mark
User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MarkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'
