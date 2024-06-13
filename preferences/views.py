from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserPreferences
from django.contrib import messages


<<<<<<< HEAD
<<<<<<< HEAD
@login_required
def index(request):
    try:
=======

def index(request):

=======
def index(request, *args):
>>>>>>> parent of b8881b3 (Fixed up HTML code)
    currency_list = []

    with open(os.path.join(settings.BASE_DIR, "currencies.json"), "r") as file:

        data = json.load(file)
        exists = UserPreferences.objects.filter(user=request.user).exists()
        user_preferences = None
        for k, v in data.items():
            currency_list.append({"name": k, "value": v})

    if exists:
<<<<<<< HEAD
>>>>>>> parent of 6352970 (chore: Clean up code formatting and remove unnecessary lines SearchExpenses.JS)
        user_preferences = UserPreferences.objects.get(user=request.user)
    except UserPreferences.DoesNotExist:
        user_preferences = UserPreferences.objects.create(
            user=request.user, currency="USD"
        )
        user_preferences.save()

    if request.method == "GET":
=======
        user_preferences = UserPreferences.objects.get(user=request.user)

    if request.method == "GET":

>>>>>>> parent of b8881b3 (Fixed up HTML code)
        return render(
            request, "expenses/index.html", {"currency": user_preferences.currency}
        )
    else:
<<<<<<< HEAD
        currency = request.POST.get("currency", "USD")
        if currency:
            user_preferences.currency = currency
            user_preferences.save()
            messages.success(request, "Currency preferences updated successfully.")
        return redirect("expenses:index")
=======
        currency = request.POST["currency"]

        if exists:

            user_preferences.currency = currency
            user_preferences.save()
        else:
            user_preferences = UserPreferences.objects.create(user=request.user, currency=currency)
        messages.success(request, "Changes saved")
        return render(
            request,
            "preferences/index.html",
            {"currencies": currency_list, "user_preferences": user_preferences},
        )


data = json.load(open(os.path.join(settings.BASE_DIR, "currencies.json"), "r"))
>>>>>>> parent of b8881b3 (Fixed up HTML code)
