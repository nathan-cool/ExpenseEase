class MyCustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Custom adapter for handling user data during social login.

    This class extends the DefaultSocialAccountAdapter
    to include custom
    logic for saving user information obtained
    from social login providers.
    """

    def save_user(self, request, sociallogin, form=None):
        """
        Save the user data during the social login process.

        Args:
            request: The current HttpRequest object.
            sociallogin: The sociallogin instance
            containing social account information.
            form: The form instance (optional).

        Returns:
            user: The saved user instance with any custom fields set.
        """
        user = super(MyCustomSocialAccountAdapter, self).save_user(
            request, sociallogin, form
        )
        user.save()
        return user
