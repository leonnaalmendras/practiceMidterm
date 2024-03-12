from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('installation/', views.installation, name = 'installation'),
    path('configuration/', views.configuration, name = 'configuration'),
    path('automation/', views.automation, name = 'automation'),
    path('index/', views.index, name = 'index'),
]
