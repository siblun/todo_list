from django.views.generic import CreateView
from ..models import ToDoList


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
