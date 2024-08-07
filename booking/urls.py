from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_list, name='class_list'),
    path('class/<int:pk>/', views.class_detail, name='class_detail'),
    path('class/<int:pk>/book/', views.book_class, name='book_class'),
    path('class/<int:pk>/cancel/', views.cancel_booking, name='cancel_booking'),
]