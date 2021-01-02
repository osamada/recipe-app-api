from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('create/', views.CreateView, name='create'),
    path('list/', views.ListView, name='list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
