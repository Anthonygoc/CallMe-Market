from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.get_user, name='get_all_user'),
]