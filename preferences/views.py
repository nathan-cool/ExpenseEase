from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserPreferences
from django.contrib import messages


@login_required
def index(request):
    try:
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
