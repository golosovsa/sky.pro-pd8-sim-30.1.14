from django.contrib.auth import get_user_model
from rest_framework import serializers
from ad.models import Ad
User = get_user_model()


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
