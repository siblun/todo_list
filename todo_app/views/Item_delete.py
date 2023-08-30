from django.urls import reverse_lazy
from django.views.generic import DeleteView
from ..models import ToDoList, ToDoItem


class ItemDelete(DeleteView):
    """
    This class is used to delete items.

    Attributes
    ----------
    model : ToDoList
        model of ToDoList

    Methods
    ----------
    get_success_url()
        provides the view with a page to display after the item has been deleted
    get_context_data()

    """

    model = ToDoItem

    def get_success_url(self):
        """
        This function calls the list view after a successful form submit to display the full to-do list.
        """
        return reverse_lazy('list', args=[self.kwargs['list_id']])

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['todo_list'] = self.object.todo_list
        return context
