from django.db import models
from django.utils import timezone
from django.urls import reverse


def one_week_hence():
    """
    Returns the time by which the task must be completed.
    """

    return timezone.now() + timezone.timedelta(days=7)


class ToDoList(models.Model):
    """
    This class is used to add a title of task.

    Attributes
    ----------
    title : CharField
        field of task's name, it can only be unique

    Methods
    ----------
    get_absolute_url()
        returns the URL for the particular data item
    """

    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        """
        This function returns the URL for the particular data item.
        The return statement uses reverse() to avoid hard-coding the URL and its parameters.
        """

        return reverse('list', args=[self.id])

    def __str__(self):
        return self.title


class ToDoItem(models.Model):
    """
    This class is used to add a task.

    Attributes
    ----------
    title : CharField
        field of task's name
    description : TextField
        field of task's description, it may be empty
    created_date : DateTimeField
        field of task creation date
    due_date : DateTimeField
        time which task can be completed
    todo_list : ForeignKey
        a foreign key that links a ToDoItem back to its ToDoList

    Methods
    ----------
    get_absolute_url()
        returns the URL for the particular data item
    """

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """
        This function returns the URL for the particular data item.
        The return statement uses reverse() to avoid hard-coding the URL and its parameters.
        """

        return reverse('item-update', args=[str(self.todo_list.id), str(self.id)])

    def __str__(self):
        return f'{self.title}: due {self.due_date}'

    class Meta:
        """
        This class used to set a default ordering for ToDoItem records.
        """

        ordering = ['due_date']
