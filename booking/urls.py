from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_list, name='class_list'),
    path('class/add/', views.add_class, name='add_class'),
    path('class/<int:pk>/', views.class_detail, name='class_detail'),
    path('class/<int:pk>/edit/', views.edit_class, name='edit_class'),
    path('class/<int:pk>/delete/', views.delete_class, name='delete_class'),
    path('class/<int:pk>/book/', views.book_class, name='book_class'),
    path('class/<int:pk>/cancel/', views.cancel_booking, name='cancel_booking'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('cancelled/', views.cancelled, name='cancelled'),
]