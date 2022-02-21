import inspect

from django.db import models
from django.db.models.fields import (
    BooleanField,
    CharField,
    DecimalField,
    SmallIntegerField,
    TextField,
)
from django.test import TestCase
from django.contrib.auth.models import AbstractUser

from custom_user_2 import models as student_models
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin, ResponseTestsMixin

TEACHER = "teacher"
STUDENT = "student"
ROLES = [(TEACHER, TEACHER), (STUDENT, STUDENT)]

char_fields = {
    "role": {"max_length": 7, "choices": ROLES},
    "password": {"max_length": 128}
}

date_fields = {
    "birth_date": {}
}


def get_model_attributes(*args):
    result = {}
    for arg in args:
        result.update(arg)
    return result

class StoreClassTestCase(TestCase, ResponseTestsMixin, DataBaseTestsMixin):
    def test_store_has_expected_fields(self):
        model_name = "CustomUser"
        self.model = getattr(student_models, model_name, None)
        self.assertTrue(
            self.model, f"%@Проверьте, что модель {model_name} определена в модуле"
        )
        self.assertTrue(
            inspect.isclass(self.model), f"Проверьте, что {model_name} является классом"
        )
        self.assertTrue(
            issubclass(self.model, AbstractUser),
            f"Проверьте, что класс {model_name} правильно определен в модуле",
        )

        current_fields = {field.name: field for field in self.model._meta.get_fields()}
        expected_fields = get_model_attributes(
            char_fields,
            date_fields
        )
        student_attrs_len = len(current_fields)
        expected_attrs_len = 16
        self.assertEqual(
            student_attrs_len,
            expected_attrs_len,
            (
                "%@ Проверьте, что добавили все необходимые поля в модель CustomUser."
                f" Мы насчитали у Вас {student_attrs_len}, тогда как должно быть {expected_attrs_len}"
            ),
        )

        for field_name in expected_fields:
            self.assertIn(
                field_name,
                current_fields,
                f"Проверьте, что добавили в модель поле {field_name}",
            )

        # Checking char_fields
        self.django_field_checker(current_fields, char_fields, CharField)
