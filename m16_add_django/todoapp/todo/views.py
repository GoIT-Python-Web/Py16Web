from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import TodoForm
from .models import Todo


# Create your views here.

class TodoListView(ListView):
    model = Todo
    template_name = "todo/list.html"
    context_object_name = "todo_list"
    paginate_by = 5

    def get_queryset(self):
        queryset = super(TodoListView, self).get_queryset()
        print(queryset)
        return queryset


class TodoCreateView(CreateView):
    model = Todo
    template_name = "todo/create.html"
    form_class = TodoForm
    success_url = reverse_lazy('main')


class TodoUpdateView(UpdateView):
    model = Todo
    template_name = "todo/update.html"
    fields = ('title', 'description', 'completed')
    success_url = reverse_lazy('main')


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo/delete.html"
    success_url = reverse_lazy('main')
