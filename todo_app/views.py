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


class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        'todo_list',
        'title',
        'description',
        'due_date',
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        initial_data['todo_list'] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        context['todo_list'] = todo_list
        context['title'] = 'Create a new item'
        return context

    def get_success_url(self):
        return reverse('list', args=[self.object.todo_list_id])
