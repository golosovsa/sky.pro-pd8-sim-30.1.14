from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # TEACHER = "teacher"
    # STUDENT = "student"
    # ROLES = [(TEACHER, TEACHER), (TEACHER, TEACHER)]

    store = models.CharField(max_length=4)
    # role = models.CharField(max_length=10, choices=ROLES, default=STUDENT)

    def save(self, *args, **kwargs):
        self.set_password(self.password)

        super().save()
