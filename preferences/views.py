from django.shortcuts import render
from django.views import View
import os
import json
from django.conf import settings
from .models import UserPreferences
from django.contrib import messages

# Create your views here.


def index(request):
    exists = UserPreferences.objects.get(user=request.user)

    if request.method == "GET":
        currency_list = []

        with open(os.path.join(settings.BASE_DIR, "currencies.json"), "r") as file:

            data = json.load(file)

        for k, v in data.items():
            currency_list.append({"name": k, "value": v})

        return render(request, "preferences/index.html", {"currencies": currency_list})
    else:
        currency = request.POST["currency"]
        user_preferences.currency = currency
        user_preferences.save()
        messages.success(request, "Changes saved")
        return render(request, "preferences/index.html", {"currencies": currency_list})
    
    