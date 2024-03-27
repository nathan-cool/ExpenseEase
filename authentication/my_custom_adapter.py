# my_custom_adapter.py

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MyCustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        # Custom user saving logic here
        user = super(MyCustomSocialAccountAdapter, self).save_user(request, sociallogin, form)
        # You can add custom fields from sociallogin.account.extra_data or other sources here
        # Example: user.profile.bio = sociallogin.account.extra_data.get('bio')
        user.save()
        return user
