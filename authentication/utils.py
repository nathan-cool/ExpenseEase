from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class AppTokenGenerator(PasswordResetTokenGenerator):
    """
    Custom token generator for generating password reset tokens.

    This class extends the PasswordResetTokenGenerator to create a hash value
    based on the user's active status, primary key, and a timestamp.
    """

    def _make_hash_value(self, user, timestamp):
        """
        Generate a hash value for the token.

        Args:
            user (User): The user object.
            timestamp (int): The timestamp value.

        Returns:
            str: The generated hash value.
        """
        return (
            text_type(user.is_active)
            + text_type(user.pk)
            + text_type(timestamp)
        )


token_generator = AppTokenGenerator()
