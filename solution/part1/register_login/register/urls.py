from django.urls import path

from register.views import UserCreateView

urlpatterns = [
   path('register/', UserCreateView.as_view()),
]
