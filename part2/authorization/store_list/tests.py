import factory

from django.test import TestCase
from store_list.models import Store
from ttools.skyprotests.tests_mixins import ResponseTestsMixin
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
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
STORE_LIST_URL = "/store_list/"


class RegisterClassTestCase(TestCase, ResponseTestsMixin):
    @classmethod
    def setUpClass(cls):
        super(RegisterClassTestCase, cls).setUpClass()
        UserFactory.create()
        for _ in range(10):
            StoreFactory.create()

    def setUp(self):
        self.model = User
        self.student_app = APIClient()
        self.anonymous_app = APIClient()

    def test_url_works_correct(self):
        self.url = TOKEN_URL
        response = self.student_app.post(
                self.url,
                data={
                    "username": "test_user",
                    "password": "P$ssW0RD",
                }
            )
        token = response.data.get("token", None)
        user = User.objects.get(username="test_user")
        self.student_app.force_authenticate(user=user, token=token)
        self.url = STORE_LIST_URL
        test_options = {
            "url": self.url,
            "method": "GET",
            "code": [200],
            "student_response": self.student_app.get(
                self.url,
            ),
            "expected": list,
            "django_mode": True,
            "text": "при запросе от аутентифицированного пользователя",
        }

        response = self.check_status_code_jsonify_and_expected(**test_options)
        obj = response.json()[0]
        expected_attributes = ("id", "name", "address", "open_hour", "close_hour")
        self.check_expected_attributes(obj, expected_attributes)
        test_options["student_response"] = self.anonymous_app.get(self.url)
        test_options["code"] = [403, ]
        test_options["expected"] = dict
        test_options["text"] = "при запросе от не аутентифицированного пользователя"
        self.check_status_code_jsonify_and_expected(**test_options)
