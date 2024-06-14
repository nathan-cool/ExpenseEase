from django.shortcuts import render
from django.conf import settings
from .models import UserPreferences
from django.contrib import messages
import os
import json


def index(request):
    """
    View function for the index page of the preferences app.

    This function handles both GET and POST requests. It loads a list of
    currencies from a JSON file
    and checks if the user has existing preferences.
    Depending on the request method, it either renders the preferences page
    with the current settings or updates the user's preferences.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with the rendered template.
    """
    currency_list = []

    # Load currency data from the JSON file
    with open(os.path.join(settings.BASE_DIR, "currencies.json"), "r") as file:
        data = json.load(file)
        exists = UserPreferences.objects.filter(user=request.user).exists()
        user_preferences = None
        for k, v in data.items():
            currency_list.append({"name": k, "value": v})

    if exists:
        user_preferences = UserPreferences.objects.get(user=request.user)

    if request.method == "GET":
        # Render the preferences page for GET requests
        return render(
            request,
            "preferences/index.html",
            {"currencies": currency_list, "user_preferences": user_preferences},
        )
    else:
        # Update user preferences for POST requests
        currency = request.POST["currency"]

        if exists:
            user_preferences.currency = currency
            user_preferences.save()
        else:
            user_preferences = UserPreferences.objects.create(
                user=request.user, currency=currency
            )

        messages.success(request, "Changes saved")

        return render(
            request,
            "preferences/index.html",
            {"currencies": currency_list, "user_preferences": user_preferences},
        )
