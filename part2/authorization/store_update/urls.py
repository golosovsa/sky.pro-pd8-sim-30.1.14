from django.urls import path
from store_update import views

urlpatterns = [
   path('store_update/<int:pk>/', views.StoreUpdateView.as_view())
]
