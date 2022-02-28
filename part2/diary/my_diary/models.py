from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    TEACHER = "teacher"
    STUDENT = "student"
    ROLE = [
        (TEACHER, TEACHER),
        (STUDENT, STUDENT)
    ]

    role = models.CharField(max_length=7, choices=ROLE)


class Mark(models.Model):
    mark = models.IntegerField()
    student = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
