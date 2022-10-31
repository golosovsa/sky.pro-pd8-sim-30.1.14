from django.contrib.auth.models import User
from django.db import models


# TODO Опишите модель профиль ниже
# TODO Профиль пользователя должен иметь следующие поля
# адрес (address) длинной не более 50 символов
# телефон (phone) - номер должен храниться в формате
class Profile(User):
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
