from django.contrib import admin
from django.urls import path, include

"""
Main URL configuration for the project.

This file links the top-level URLs to the respective applications'
URL configurations.
Here's what each URL does:

- '' : Includes URLs from the expenses app.
- 'authentication/' : Includes URLs from the authentication app.
- 'preferences/' : Includes URLs from the preferences app.
- 'admin/' : Links to the Django admin site.
- 'accounts/' : Includes URLs from the allauth package.
"""

urlpatterns = [
    path("", include("expenses.urls")),
    path("authentication/", include("authentication.urls")),
    path("preferences/", include("preferences.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]
