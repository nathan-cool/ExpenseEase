import os
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from dotenv import load_dotenv
from .models import Category, Expenses
from django.shortcuts import redirect
from django.contrib import messages
import openai
import json
from django.http import JsonResponse
from preferences.models import UserPreferences
from django.core.paginator import Paginator

load_dotenv(override=True)


def search_expenses(request):
    """
    Search for expenses in the database.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    if request.method == "POST":
        search_str = json.loads(request.body).get("searchText", "")
        expenses = (
            Expenses.objects.filter(amount__istartswith=search_str, owner=request.user)
            or Expenses.objects.filter(date__istartswith=search_str, owner=request.user)
            or Expenses.objects.filter(
                category__icontains=search_str, owner=request.user
            )
            or Expenses.objects.filter(
                description__icontains=search_str, owner=request.user
            )
            or Expenses.objects.filter(
                invoice_number__icontains=search_str, owner=request.user
            )
            or Expenses.objects.filter(
                reference__icontains=search_str, owner=request.user
            )
        )
        data = expenses.values()
        return JsonResponse(list(data), safe=False)


@login_required(login_url="/authentication/login")
def index(request):
    """
    Display the expenses page.

    Args:
        request (HttpRequest): The request object.

    returns:
        HttpResponse: The response object.
    """
    # categories = Category.objects.all() ??
    expenses = Expenses.objects.filter(owner=request.user)
    paginator = Paginator(expenses, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    currency = UserPreferences.objects.get(user=request.user).currency
    context = {
        "expenses": expenses,
        "currency": currency,
        "page_obj": page_obj,
    }

    return render(request, "expenses/index.html", context)


# Add expenses
@login_required(login_url="/authentication/login")
def add_expenses(request):
    """
    Add an expense to the database.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponseRedirect: A redirect to the expenses page or an error message.
    """

    try:
        categories = Category.objects.all()
        context = {"categories": categories, "values": request.POST}
    except Exception as e:
        print(f"Error: {str(e)}")
        categories = [Food, Rent, Travel, Salary, Other]
        context = {"categories": categories, "values": request.POST}

    if request.method == "GET":
        return render(request, "expenses/add-expenses.html", context)
    try:
        if request.method == "POST":
            amount = request.POST["amount"]
            date = request.POST["date"]
            category = request.POST["category"]
            description = request.POST["description"]
            invoice_number = request.POST.get("invoice_number", " ")
            reference = request.POST.get("reference", " ")
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
            description=description,
            invoice_number=invoice_number,
            reference=reference,
        )
        messages.success(request, "Expenses saved successfully")
        return redirect("expenses")
    except Exception as e:
        print(f"Error: {str(e)}")
        messages.error(request, "An error occurred while saving the expenses")


# Edit expenses
@login_required(login_url="/authentication/login")
def expense_edit(request, id):
    """
    Edit an expense in the database.

    Args:
        request (HttpRequest): The request object.
        id (int): The ID of the expense to edit.

    Returns:
        HttpResponseRedirect: A redirect to the expenses page or an error message.
    """

    expense = Expenses.objects.get(pk=id)
    categories = Category.objects.all()

    # Retrieve the current category of the expense
    current_category = expense.category
    formatted_date = expense.date.strftime("%Y-%m-%d")

    context = {
        "expense": expense,
        "invoice_number": expense.invoice_number,
        "reference": expense.reference,
        "amount": expense.amount,
        "categories": categories,
        "current_category": current_category,
        "date": formatted_date,
        "description": expense.description,
    }

    if request.method == "GET":
        return render(request, "expenses/edit-expense.html", context)
    try:
        if request.method == "POST":

            amount = request.POST.get("amount")
            date = request.POST.get("date")
            category = request.POST.get("category")
            description = request.POST.get("description")
            invoice_number = request.POST.get("invoice_number")
            reference = request.POST.get("reference")
            # x = expense.amount, expense.date,  expense.category, expense.description, expense.invoice_number, expense.reference ??

            if not amount:
                messages.error(request, "Amount is required")
                return render(request, "expenses/add-expenses.html", context)

            if not date:
                messages.error(request, "Date is required")
                return render(request, "expenses/add-expenses.html", context)

            if not description:
                messages.error(request, "Description is required")
                return render(request, "expenses/add-expenses.html", context)

            if not category:
                messages.error(request, "Category is required")
                return render(request, "expenses/add-expenses.html", context)

            expense.amount = amount
            expense.date = date
            expense.category = category
            expense.description = description
            expense.invoice_number = invoice_number
            expense.reference = reference

            expense.save()
            messages.success(request, "Expense Saved Successfully")
            return redirect("expenses")
    except Exception as e:
        print(f"Error: {str(e)}")
        messages.error(request, "An error occurred while saving the expenses")
        return render(request, "expenses/edit-expense.html", context)


# Delete expenses
@login_required(login_url="/authentication/login")
def delete_expense(request, id):
    """
    Delete an expense from the database.

    Args:
        request (HttpRequest): The request object.
        id (int): The ID of the expense to delete.

    Returns:
        HttpResponseRedirect: A redirect to the expenses page or an error message.
    """

    if request.method == "GET":
        try:
            expense = Expenses.objects.get(pk=id)
            expense.delete()
            messages.success(request, "Expense deleted successfully")
            return redirect("expenses")
        except Exception as e:
            print(f"Error: {str(e)}")
            messages.error(request, "An error occurred while deleting the expense")
            return redirect("expenses")


print("Using API Key:", os.getenv("OPENAI_API_KEY"))  # Temporarily check the API key


# Generate description
def create_assistant(expense_details):
    """
    Generate a description for an expense based on the provided details using OpenAI ChatCompletion API.

    Args:
        expense_details (dict): A dictionary containing expense details.

    Returns:
        str: The generated expense description or an error message.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Generate a description for this expense based on the provided details",
                },
                {
                    "role": "user",
                    "content": f"Amount: {expense_details['amount']}\nInvoice Number: {expense_details['invoice_number']}\nReference: {expense_details['reference']}\nCategory: {expense_details['category']}\nDate: {expense_details['date']}",
                },
            ],
            api_key=os.getenv("OPENAI_API_KEY"),
        )
        print("API Response:", response)
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error: {str(e)}")
        return "An error occurred while generating the description."


def generate_description(request, id):
    """
    Generate a description for an expense based on the provided details.

    args:
        request (HttpRequest): The request object.

    returns:
        HttpResponse: The response object.
    """

    expense = get_object_or_404(Expenses, pk=id)
    expense_details = {
        "amount": expense.amount,
        "invoice_number": expense.invoice_number,
        "reference": expense.reference,
        "category": expense.category,
        "date": expense.date.strftime("%Y-%m-%d"),
    }
    generated_description = create_assistant(expense_details)

    expense = Expenses.objects.get(pk=id)
    categories = Category.objects.all()

    # Retrieve the current category of the expense
    current_category = expense.category
    formatted_date = expense.date.strftime("%Y-%m-%d")

    context = {
        "description": generated_description,
        "expense": expense,
        "invoice_number": expense.invoice_number,
        "reference": expense.reference,
        "amount": expense.amount,
        "categories": categories,
        "current_category": current_category,
        "date": formatted_date,
    }

    if request.method == "GET":
        return render(request, "expenses/edit-expense.html", context)
