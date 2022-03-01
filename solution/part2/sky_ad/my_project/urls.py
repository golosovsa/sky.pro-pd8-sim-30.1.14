from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
# TODO здесь можно подключить urls Ваших приложений

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", views.obtain_auth_token),
    path("", include("users.urls")),
    path("", include("ad.urls"))
]
