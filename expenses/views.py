from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category, Expenses
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    categories = Category.objects.all()
    expenses = Expenses.objects.filter(owner=request.user)

    context = {
        "expenses": expenses,
    }

    return render(request, "expenses/index.html", context)

def add_expenses(request):
    categories = Category.objects.all()
    context = {
            "categories": categories,
            "values": request.POST
        }

    if request.method == "GET":
        return render(request, "expenses/add-expenses.html", context)

    if request.method == "POST":
        amount = request.POST["amount"]
        date = request.POST["date"]
        category = request.POST["category"]
        description = request.POST["description"]
        owner = request.user

        if not amount:
            messages.error(request, "Amount is required")
            return render(request, "expenses/add-expenses.html", context)

        if not date:
            messages.error(request, "Date is required")
            return render(request, "expenses/add-expenses.html", context)

        if not category:
            messages.error(request, "Category is required")
            return render(request, "expenses/add-expenses.html", context)

        if not description:
            messages.error(request, "Description is required")
            return render(request, "expenses/add-expenses.html", context)

        Expenses.objects.create(
            owner=owner,
            amount=amount,
            date=date,
            category=category,
            description=description
        )
        messages.success(request, "Expenses saved successfully")
        return redirect('expenses')


def expense_edit(request, id):
    expense = Expenses.objects.get(pk=id)

    context = {"expense": expense, "values": expense}

    if request.method == "GET":
        return render(request, "expenses/edit-expense.html", context)
    else:
        messages.info(request, "Expense not edited")
        return render(request, "expenses/edit-expense.html", context)
