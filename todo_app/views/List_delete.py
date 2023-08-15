from django.urls import reverse_lazy
from django.views.generic import DeleteView
from ..models import ToDoList


class ListDelete(DeleteView):
    """
    This class is used to delete to-do lists.

    Attributes
    ----------
    model : ToDoList
        model of ToDoList
    success_url
        returns url as url attribute of generic view based on class
    """

    model = ToDoList
    success_url = reverse_lazy('index')
