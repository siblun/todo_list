from django.apps import AppConfig


class TodoAppConfig(AppConfig):
    """
        This class is used to configure the application.

        Attributes
        ----------
        default_auto_field : str
            the implicit primary key type to add to models within this app
        name : str
            defines which application the configuration applies to
        """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo_app'
