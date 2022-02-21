from django.urls import path

from register.views import UserCreateView
from rest_framework.authtoken import views

urlpatterns = [
   path('register/', UserCreateView.as_view()),
   path('login/', views.obtain_auth_token),
]
