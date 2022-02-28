from django.db import models
from django.db.models import CASCADE
from django.contrib.auth import get_user_model

User = get_user_model()


class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
