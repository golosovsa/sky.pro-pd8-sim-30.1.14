from django.urls import path
from ad import views
# TODO здесь можно подключить urls Ваших приложений

urlpatterns = [
    path("ad/<int:pk>/", views.AdUpdateView.as_view())
]
