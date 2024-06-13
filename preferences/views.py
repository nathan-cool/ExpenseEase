from django.shortcuts import render
from django.views import View
import os
import json
from django.conf import settings
from .models import UserPreferences
from django.contrib import messages

# Create your views here.


def index(request, *args):
    currency_list = []

    with open(os.path.join(settings.BASE_DIR, "currencies.json"), "r") as file:
        data = json.load(file)
        for k, v in data.items():
            currency_list.append({"name": k, "value": v})

    # Check if UserPreferences exists for the user
    user_preferences = UserPreferences.objects.filter(user=request.user).first()

    if request.method == "GET":
        # If user_preferences is None, set a default value
        if user_preferences is None:
            user_preferences = UserPreferences(
                user=request.user, currency="USD"
            )  # Default currency
            user_preferences.save()

        return render(
            request,
            "preferences/index.html",
            {"currencies": currency_list, "user_preferences": user_preferences},
        )
    else:
        currency = request.POST.get("currency")

        if user_preferences:
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


data = json.load(open(os.path.join(settings.BASE_DIR, "currencies.json"), "r"))
