from django.contrib import admin
from django.urls import include, path

# TODO здесь можно подключить urls Ваших приложений

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("my_diary.urls")),
]
