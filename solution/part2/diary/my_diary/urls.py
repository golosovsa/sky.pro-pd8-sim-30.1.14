from django.urls import path
from my_diary.views import MarkCreateView
from rest_framework.authtoken import views

urlpatterns = [
   path('diary/', MarkCreateView.as_view()),
   path('login/', views.obtain_auth_token),
]
