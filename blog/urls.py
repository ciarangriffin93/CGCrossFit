from django.urls import path
from . import views

from .views import (
    NewComment,
    EditComment,
    DeleteComment,
)

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('<slug:slug>/', views.event_detail, name='event_detail'),
    path('like/<slug:slug>/', views.event_like, name='event_like'),
    path('comment/<int:pk>/', views.NewComment.as_view(), name='new_comment'),
    path('edit/<int:pk>/', views.EditComment.as_view(), name='edit_comment'),
    path('delete/<int:pk>/', views.DeleteComment.as_view(), name='delete_comment'),
]