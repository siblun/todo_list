from django.urls import reverse
from django.views.generic import UpdateView
from ..models import ToDoList, ToDoItem


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
