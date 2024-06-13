from django.shortcuts import render
from django.views import View
import os
import json
from django.conf import settings
from .models import UserPreferences
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


def index(request, *args):
    currency_list = []

    with open(os.path.join(settings.BASE_DIR, "currencies.json"), "r") as file:
        data = json.load(file)
        for k, v in data.items():
            currency_list.append({"name": k, "value": v})

    try:
        user_preferences = UserPreferences.objects.get(user=request.user)
    except UserPreferences.DoesNotExist:
        user_preferences = None

    if request.method == "GET":
        if user_preferences is None:
            user_preferences = UserPreferences.objects.create(
                user=request.user, currency="USD"
            )

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
