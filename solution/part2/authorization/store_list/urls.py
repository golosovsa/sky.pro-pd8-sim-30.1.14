from django.urls import path
from store_list import views

urlpatterns = [
   path('store_list/', views.StoreListView.as_view()),
]
