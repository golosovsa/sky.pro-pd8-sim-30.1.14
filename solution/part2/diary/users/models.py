from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    store = models.CharField(max_length=4)

    def save(self, *args, **kwargs):
        self.set_password(self.password)

        super().save()
