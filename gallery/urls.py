from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('add/', views.add_media, name='add_media'),
    path('edit/<int:pk>/', views.edit_media, name='edit_media'),
    path('delete/<int:pk>/', views.delete_media, name='delete_media'),
    path('media/<int:pk>/', views.media_detail, name='media_detail'),
]