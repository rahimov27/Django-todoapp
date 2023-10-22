from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.todo_view),
    path("<id>/delete", views.delete_view, name="delete_view"),
]
