from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from .models import ToDoList, ToDoItem


class ListCreate(CreateView):
    model = ToDoList
    fields = ['title']

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context['title'] = 'Add a new list'
        return context
