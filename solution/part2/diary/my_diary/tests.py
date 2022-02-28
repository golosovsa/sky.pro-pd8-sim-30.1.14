import factory

from django.test import TestCase
from ttools.skyprotests.tests_mixins import ResponseTestsMixin
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APIRequestFactory
from my_diary.models import Mark
User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    role = "teacher"
    username = "test_user"
    email = "test_sky@pro.com"


class MarkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Mark

    mark = 5


TOKEN_URL = "/login/"
DIARY_URL = "/diary/"


class RegisterClassTestCase(TestCase, ResponseTestsMixin):
    @classmethod
    def setUpClass(cls):
        super(RegisterClassTestCase, cls).setUpClass()
        User.objects.create_user(username="teacher", password="skypro", role="teacher")
        User.objects.create_user(username="student", password="skypro", role="student")
        for _ in range(10):
            MarkFactory.create(student=User.objects.get(id=2))

    def setUp(self):
        self.model = User
        self.student_app = APIClient()
        self.teacher_app = APIClient()
        self.anonymous_app = APIClient()

    def test_teacher_url_works_correct(self):
        user = User.objects.get(username='teacher')
        response = self.teacher_app.post(
                TOKEN_URL,
                {
                 "username": "teacher",
                 "password": "skypro"
                },
                format="json"
            )
        token = response.data.get("token", None)
        self.teacher_app.force_authenticate(user=user, token=token)

        # ЗАПРОС от пользователя-учителя
        self.url = DIARY_URL
        response = self.teacher_app.post(
            self.url,
            data={
                "mark": 5,
                "student": 2
            }
        )
        self.assertTrue(
            response.status_code in [200, 201],
            f"Проверьте, что учитель может поставить оценку студенту (POST-запрос с токеном учителя на адрес {DIARY_URL} возвращает код 201)"
        )

    def test_anonymous_url_works_correct(self):
        response = self.anonymous_app.patch(
            DIARY_URL,
            data={
                "mark": 5,
                "student": 2
            }
        )
        self.assertTrue(
            response.status_code == 403,
            f"Проверьте, что если пользователь не аутентифицирован, то он не может создать запись с отметкой"
        )

    def test_student_url_works_correct(self):
        response = self.student_app.post(
                TOKEN_URL,
                {
                    "username": "student",
                    "password": "skypro",
                }
            )
        token = response.data.get("token", None)
        user = User.objects.get(username="student")
        self.student_app.force_authenticate(user=user, token=token)
        response = self.student_app.post(
            DIARY_URL,
            data={
                "mark": 5,
                "student": 2
            }
        )
        self.assertTrue(
            response.status_code == 403,
            f"Проверьте, что если пользователь - cтудент,то он не может создать запись с отметкой"
        )
