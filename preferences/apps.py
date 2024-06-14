from django.apps import AppConfig


class UserpreferencesConfig(AppConfig):
    """
    Configuration class for the 'preferences' application.

    This class is used to configure the application-specific settings
    and properties for the 'preferences' app in a Django project.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "preferences"
