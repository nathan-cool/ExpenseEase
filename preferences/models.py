from django.db import models
from django.contrib.auth.models import User


class UserPreferences(models.Model):
    """
    UserPreferences model to store additional preferences for a user.

    Attributes:
        user (OneToOneField): A one-to-one relationship to the User model.
        currency (CharField): A field to store the
        preferred currency of the user.
        Default is "EUR".

    Methods:
        __str__: Returns a string representation of the user preferences.
    """

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=255, default="EUR")

    def __str__(self):
        """
        Returns a string representation of the user preferences.

        Returns:
            str: A string in the format 'Preferences for <username>'.
        """
        return f"Preferences for {self.user.username}"
