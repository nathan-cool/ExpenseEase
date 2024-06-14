from django.urls import path
from . import views

"""
URLs for the user preferences app.

This file links up the URLs to the views.
Right now, we've got:

- '' : Goes to the index view, named 'preferences'.
"""

urlpatterns = [
    path("", views.index, name="preferences"),
]
