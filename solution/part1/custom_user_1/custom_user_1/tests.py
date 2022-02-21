import inspect

from django.db.models.fields import (
    CharField,
)
from django.test import TestCase

from custom_user_1 import models as student_models
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin, ResponseTestsMixin
from django.contrib.auth.models import User
char_fields = {
    "phone": {"max_length": 12},
    "address": {"max_length": 50},
}

def get_model_attributes(*args):
    result = {}
    for arg in args:
        result.update(arg)
    return result


class StoreClassTestCase(TestCase, ResponseTestsMixin, DataBaseTestsMixin):
    def test_store_has_expected_fields(self):
        model_name = "Profile"
        self.model = getattr(student_models, model_name, None)
        self.assertTrue(
            self.model, f"%@Проверьте, что модель {model_name} определена в модуле models приложения custom_user_1"
        )
        self.assertTrue(
            inspect.isclass(self.model), f"Проверьте, что {model_name} является классом"
        )
        self.assertTrue(
            issubclass(self.model, User),
            f"Проверьте, что класс {model_name} унаследован от модели User",
        )

        current_fields = {field.name: field for field in self.model._meta.get_fields()}
        expected_fields = get_model_attributes(
            char_fields
        )

        for field_name in expected_fields:
            self.assertIn(
                field_name,
                current_fields,
                f"Проверьте, что добавили в модель поле {field_name}",
            )

        self.django_field_checker(current_fields, char_fields, CharField)
