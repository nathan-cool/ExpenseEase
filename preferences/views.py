from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserPreferences
from django.contrib import messages


<<<<<<< HEAD
@login_required
def index(request):
    try:
=======

def index(request):

    currency_list = []

    with open(os.path.join(settings.BASE_DIR, "currencies.json"), "r") as file:

        data = json.load(file)
        exists = UserPreferences.objects.filter(user=request.user).exists()
        user_preferences = None
        for k, v in data.items():
            currency_list.append({"name": k, "value": v})

    if exists:
>>>>>>> parent of 6352970 (chore: Clean up code formatting and remove unnecessary lines SearchExpenses.JS)
        user_preferences = UserPreferences.objects.get(user=request.user)
    except UserPreferences.DoesNotExist:
        user_preferences = UserPreferences.objects.create(
            user=request.user, currency="USD"
        )
        user_preferences.save()

    if request.method == "GET":
        return render(
            request, "expenses/index.html", {"currency": user_preferences.currency}
        )
    else:
        currency = request.POST.get("currency", "USD")
        if currency:
            user_preferences.currency = currency
            user_preferences.save()
            messages.success(request, "Currency preferences updated successfully.")
        return redirect("expenses:index")
