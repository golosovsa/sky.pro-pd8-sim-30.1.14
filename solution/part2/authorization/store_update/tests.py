import factory

from django.test import TestCase
from store_update.models import Store
from ttools.skyprotests.tests_mixins import ResponseTestsMixin
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APIRequestFactory
import json
User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "test_user"
    password = "P$ssW0RD"
    email = "test_sky@pro.com"


class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Store

    name = "test_store"
    address = "test_address"
    open_hour = 8
    close_hour = 20


TOKEN_URL = "/login/"
STORE_LIST_URL = "/store_update/1/"




class RegisterClassTestCase(TestCase, ResponseTestsMixin):
    @classmethod
    def setUpClass(cls):
        super(RegisterClassTestCase, cls).setUpClass()
        UserFactory.create()
        UserFactory.create(username="test_admin", is_staff=True)
        for _ in range(10):
            StoreFactory.create()

    def setUp(self):
        self.model = User
        self.student_app = APIClient()
        self.anonymous_app = APIClient()


    def test_url_works_correct(self):
        exception_text = f"при PATCH-запросе на адрес {STORE_LIST_URL} возвращается код 403"
        response = self.student_app.post(
                TOKEN_URL,
                data={
                    "username": "test_user",
                    "password": "P$ssW0RD",
                }
            )
        token = response.data.get("token", None)
        user = User.objects.get(username="test_user")
        self.student_app.force_authenticate(user=user, token=token)

        # ЗАПРОС от аутентифицированного пользователя
        self.url = STORE_LIST_URL
        response = self.student_app.patch(
            self.url,
            data={
                "address": "new_name"
            }
        )
        self.assertTrue(
            response.status_code == 403,
            f"Проверьте, что если пользователь не имеет прав администратора, то {exception_text}"
        )

        # ЗАПРОС от не аутентифицированного пользователя
        response = self.anonymous_app.patch(
            self.url,
           {"name": "new_name"}
        )
        self.assertTrue(
            response.status_code == 403,
            f"Проверьте, что если пользователь не аутентифицирован, то {exception_text}"
        )

        # запрос от администратора
        self.url = TOKEN_URL
        response = self.student_app.post(
                self.url,
                {
                    "username": "test_admin",
                    "password": "P$ssW0RD",
                }
            )
        token = response.data.get("token", None)
        user = User.objects.get(username="test_admin")
        self.student_app.force_authenticate(user=user, token=token)
        self.url = STORE_LIST_URL
        expected_values = {
            "name": "new_name",
            "address": "new_address",
            "open_hour": 0,
            "close_hour": 0
        }
        test_options = {
            "url": self.url,
            "method": "GET",
            "code": [200],
            "student_response": self.student_app.patch(
                self.url,
                expected_values,
                forman="json",

            ),
            "expected": list,
            "django_mode": True,
            "text": "при запросе от администратора",
            "debug_mode": True
        }
        response = self.check_status_code_jsonify_and_expected(**test_options)
        obj = response.json()
        expected_attributes = ("id", "name", "address", "open_hour", "close_hour")
        self.check_expected_attributes(obj, expected_attributes)
        for key, value in expected_values.items():
            self.assertTrue(
                obj.get(key) == value,
                "Проверьте, что при PATCH-запросе на адрес /store_update/{id}/ в ответе содержатся обновленные данные"
            )