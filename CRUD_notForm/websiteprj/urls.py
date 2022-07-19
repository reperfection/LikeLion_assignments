"""websiteprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import websiteapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', websiteapp.views.main, name='main'),
    path('write/', websiteapp.views.write, name='write'),
    path('write/create/', websiteapp.views.create, name='create'),
    path('read/', websiteapp.views.read, name='read'),
    path('detail/<str:id>', websiteapp.views.detail, name='detail'),
    path('edit/<str:id>', websiteapp.views.edit, name='edit'),
    path('update/<str:id>', websiteapp.views.update, name='update'),
    path('delete/<str:id>', websiteapp.views.delete, name='delete'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
