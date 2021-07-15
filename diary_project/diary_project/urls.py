"""diary_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include
from Diary import views as D
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',D.home, name='home'),
    path('diary/create', D.create ,name='create'),
    path('<str:id>', D.detail, name='detail'),
    path('delete/<str:id>', D.delete, name='delete'),
    path('accounts/', include('allauth.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
