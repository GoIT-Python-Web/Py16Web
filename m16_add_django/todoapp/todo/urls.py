from django.urls import path

from . import views

urlpatterns = [
    path("", views.TodoListView.as_view(), name="main"),
    path("todo/create", views.TodoCreateView.as_view(), name="create-todo"),
    path("todo/edit/<pk>", views.TodoUpdateView.as_view(), name="edit-todo"),
    path("todo/delete/<pk>", views.TodoDeleteView.as_view(), name="delete-todo")
]
