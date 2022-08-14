from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.main, name='main'),
    path('write/', views.write, name='write'),
    path('read/', views.read, name='read'),
    path('detail/<str:id>/', views.detail, name='detail'),
    path('edit/<str:id>/', views.edit, name='edit'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('hashtag/', views.hashtag, name='hashtag'),    
]