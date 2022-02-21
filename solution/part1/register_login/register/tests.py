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


TEST_URL = "/register/"


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
            "method": "GET",
            "code": [200, 201],
            "student_response": self.student_app.post(
                self.url,
                data={
                    "username": "test_user_2",
                    "password": "P4s$W0RD",
                    "email": "test@skypro.ru",
                    "store": "test"
                }
            ),
            "expected": dict,
            "django_mode": True,
        }

        response = self.check_status_code_jsonify_and_expected(**test_options)
        obj = response.json()
        expected_attributes = (field.name for field in self.model._meta.fields)
        self.check_expected_attributes(obj, expected_attributes)
        self.assertTrue(
            User.objects.filter(username="test_user_2").count() == 1,
            "Проверьте что при POST-запросе на адрес /register/ c необходимыми данными пользователь создается в БД"
        )