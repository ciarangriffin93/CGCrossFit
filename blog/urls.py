from . import views
from django.urls import path

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('<slug:slug>/', views.event_detail, name='event_detail'),
    path('like/<slug:slug>/', views.event_like, name='event_like'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]