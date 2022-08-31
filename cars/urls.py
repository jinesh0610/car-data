from django.contrib import admin
from django.urls import path
from . import views

app_name = "cars"



urlpatterns = [
    path('', views.list, name = 'list'),
    path('add/', views.add, name = 'add'),
    path('del/', views.dele, name = 'dele'),
]