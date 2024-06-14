from django.apps import AppConfig


class ExpensesConfig(AppConfig):
    """
    Configuration class for the Expenses application.

    This class sets the default field type for auto-generated primary keys
    and specifies the name of the application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "expenses"
