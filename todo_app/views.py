from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from .models import ToDoList, ToDoItem


class ListCreate(CreateView):
    """
    This class defines a form containing the sole public ToDoList attribute, its title.

    Attributes
    ----------
    model : ToDoList
        model of ToDoList
    fields:
        name of the form fields

    Methods
    ----------
    get_context_data()
        returns the form's title
    """

    model = ToDoList
    fields = ['title']

    def get_context_data(self):
        """
        This function returns a form's title.
        """

        context = super(ListCreate, self).get_context_data()
        context['title'] = 'Add a new list'
        return context


class ItemCreate(CreateView):
    """
    This class generates a form to create an item.

    Attributes
    ----------
    model : ToDoList
        model of ToDoList
    fields:
        names of the form fields

    Methods
    ----------
    get_initial()
        returns the initial data for 'todo_list' field
    get_context_data()
        returns the form's title
    get_success_url()
        provides the view with a page to display after the new item has been created
    """

    model = ToDoItem
    fields = [
        'todo_list',
        'title',
        'description',
        'due_date',
    ]

    def get_initial(self):
        """
        This function returns an initial data of form.
        """

        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        initial_data['todo_list'] = todo_list
        return initial_data

    def get_context_data(self):
        """
        This function returns a form's title.
        """

        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        context['todo_list'] = todo_list
        context['title'] = 'Create a new item'
        return context

    def get_success_url(self):
        """
        This function calls the list view after a successful form submit to display the full to-do list
        containing the new item.
        """

        return reverse('list', args=[self.object.todo_list_id])


class ItemUpdate(UpdateView):
    """
       This class is used to update items.

       Attributes
       ----------
       model : ToDoList
           model of ToDoList
       fields:
           names of the form fields

       Methods
       ----------
       get_context_data()
           returns the form's title
       get_success_url()
           provides the view with a page to display after the new item has been created
       """

    model = ToDoItem
    fields = [
        'todo_list',
        'title',
        'description',
        'due_date'
    ]

    def get_context_data(self):
        """
        This function returns a form's title.
        """

        context = super(ItemUpdate, self).get_context_data()
        context['todo_list'] = self.object.todo_list
        context['title'] = 'Edit item'
        return context

    def get_success_url(self):
        """
        This function calls the list view after a successful form submit to display the full to-do list
        containing the new item.
        """

        return reverse('list', args=[self.object.todo_list_id])
