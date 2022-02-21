from django.contrib.auth.models import User
from django.db import models


class Profile(User):
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=50)
