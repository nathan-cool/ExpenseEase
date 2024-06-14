from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    Configuration class for the Authentication application.

    This class sets the default field type 
    for auto-generated primary keys
    and specifies the name of the application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "authentication"
