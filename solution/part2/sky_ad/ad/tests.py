import factory

from django.test import TestCase
from ttools.skyprotests.tests_mixins import ResponseTestsMixin
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APIRequestFactory
from ad.models import Ad
User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    phone = "+79775677777"
    username = "test_user"
    email = "test_sky@pro.com"


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "test_name"
    description = "test_description"
    price = 10000


TOKEN_URL = "/login/"
FIRST_AD_URL = "/ad/1/"
SECOND_AD_URL = "/ad/2/"


class RegisterClassTestCase(TestCase, ResponseTestsMixin):
    @classmethod
    def setUpClass(cls):
        super(RegisterClassTestCase, cls).setUpClass()
        user_1 = User.objects.create_user(username="sergey", password="skypro")
        user_2 = User.objects.create_user(username="nikita", password="skypro")
        AdFactory.create(user=User.objects.get(id=1))
        AdFactory.create(user=User.objects.get(id=2))

    def setUp(self):
        self.model = User
        self.first_user_app = APIClient()
        self.second_user_app = APIClient()
        self.anonymous_app = APIClient()

    def test_user_url_works_correct(self):
        user = User.objects.get(username='sergey')
        response = self.first_user_app.post(
                TOKEN_URL,
                {
                 "username": "sergey",
                 "password": "skypro"
                },
                format="json"
            )
        token = response.data.get("token", None)
        self.first_user_app.force_authenticate(user=user, token=token)
        # ЗАПРОС от пользователя-учителя
        response = self.first_user_app.patch(
            FIRST_AD_URL,
            data={
                "id": 1,
                "name": "new_name",
                "description": "new_description"
            }
        )

        self.assertTrue(
            response.status_code == 200,
            "Проверьте, что если пользователю принадлежит объявление то он может его изменить (при PATCH-запросе на адрес /ad/{id}/ возвращается код 200)"
        )

        response = self.first_user_app.patch(
            SECOND_AD_URL,
            data={
                "id": 2,
                "name": "new_name",
                "description": "new_description"
            }
        )

        self.assertTrue(
            response.status_code == 403,
            "Проверьте, что если пользователю не принадлежит объявление то он не может его изменить (при PATCH-запросе на адрес /ad/{id}/ возвращается код 403)"
        )

    def test_anonymous_url_works_correct(self):
        response = self.anonymous_app.patch(
            SECOND_AD_URL,
            data={
                "id": 1,
                "name": "new_name",
                "description": "new_description"
            }
        )
        self.assertTrue(
            response.status_code == 403,
            "Проверьте, что анонимный пользователь не может изменить объявление (при PATCH-запросе на адрес /ad/{id}/ возвращается код 403)"
        )
