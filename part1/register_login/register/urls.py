from django.urls import path
from rest_framework.authtoken import views

from register.views import UserCreateView

urlpatterns = [
   path('register/', UserCreateView.as_view()),
   path('login/', views.obtain_auth_token),
]
