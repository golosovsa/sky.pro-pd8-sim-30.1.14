from django.contrib.auth.models import AbstractUser
from django.db import models


# TODO опишите модель кастомного пользователя ниже
class CustomUser(AbstractUser):
    TEACHER = "teacher"
    STUDENT = "student"
    ROLE = [("teacher", TEACHER), ("student", STUDENT)]

    role = models.CharField(max_length=7, choices=ROLE)
    birth_date = models.DateField()
