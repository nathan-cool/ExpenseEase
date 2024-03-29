from django.shortcuts import render
from django.views import View
import os
import json
from django.conf import settings
from .models import UserPreferences
from django.contrib import messages

# Create your views here.


def index(request):

    currency_list = []

    with open(os.path.join(settings.BASE_DIR, "currencies.json"), "r") as file:

        data = json.load(file)
        exists = UserPreferences.objects.filter(user=request.user).exists()
        user_preferences = None
        for k, v in data.items():
            currency_list.append({"name": k, "value": v})

    if exists:
        user_preferences = UserPreferences.objects.get(user=request.user)

    if request.method == "GET":

        return render(
            request,
            "preferences/index.html",
            {"currencies": currency_list, "user_preferences": user_preferences},
        )
    else:
        currency = request.POST["currency"]

        if exists:

            user_preferences.currency = currency
            user_preferences.save()
        else:
            user_preferences = UserPreferences.objects.create(user=request.user, currency=currency)
        messages.success(request, "Changes saved")
        return render(
                request, "preferences/index.html", {"currencies": currency_list}
            )
