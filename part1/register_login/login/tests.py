import factory
from register.models import User
from django.test import TestCase
from django.test.client import Client
from ttools.skyprotests.tests_mixins import ResponseTestsMixin


class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    store = "test"
    username = "test_user"
    password = "P$ssW0RD"
    email = "test_sky@pro.com"


TEST_URL = "/login/"


class RegisterClassTestCase(TestCase, ResponseTestsMixin):
    @classmethod
    def setUpClass(cls):
        super(RegisterClassTestCase, cls).setUpClass()
        StoreFactory.create()

    def setUp(self):
        self.model = User
        self.student_app = Client()

    def test_url_works_correct(self):
        self.url = TEST_URL
        test_options = {
            "url": self.url,
            "method": "POST",
            "code": [200],
            "student_response": self.student_app.post(
                self.url,
                data={
                    "username": "test_user",
                    "password": "P$ssW0RD",
                }
            ),
            "expected": dict,
            "django_mode": True,
        }

        response = self.check_status_code_jsonify_and_expected(**test_options)
        obj = response.json()
        expected_attributes = ("token", )
        self.check_expected_attributes(obj, expected_attributes)
