# coding=utf-8

from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name="index"),
    path('homepage/games/', views.games, name="games"),
]
