from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    TEACHER = "teacher"
    STUDENT = "student"
    ROLES = [(TEACHER, TEACHER), (STUDENT, STUDENT)]

    birth_date = models.DateField()
    role = models.CharField(max_length=7, choices=ROLES)

    def save(self, *args, **kwargs):
        self.set_password(self.password)

        super().save()
