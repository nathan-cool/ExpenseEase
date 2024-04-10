from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category, Expenses
from django.shortcuts import redirect
from django.contrib import messages
import openai


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
        invoice_number = request.POST.get("invoice_number", " ")
        reference = request.POST.get("reference"," ")
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
        return redirect('expenses')


def expense_edit(request, id):

    expense = Expenses.objects.get(pk=id)

    context = {
        "expense": expense,
        "values": expense,
        "categories": Category.objects.all(),
    }

    if request.method == "GET":
        return render(request, "expenses/edit-expense.html", context)

    if request.method == "POST":

        amount = request.POST.get("amount")
        date = request.POST.get("date")
        category = request.POST.get("category")
        description = request.POST.get("description")
        invoice_number = request.POST.get("invoice_number")
        reference = request.POST.get("reference")

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
        return render(request, "expenses/index.html", context)

    else:
        messages.info(request, "Expense not edited")
        return render(request, "expenses/edit-expense.html", context)


def delete_expense(request, id):
    if request.method == "GET":
        
    
        expense = Expenses.objects.get(pk=id)
        expense.delete()
        messages.success(request, "Expense deleted successfully")
        return redirect('expenses')
    




def create_assistant(expense_details):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Generate a description for this expense based on the provided details"},
            {"role": "user", "content": expense_details}
        ]
    )
    return response.choices[0].message.content.strip()

def generate_description(request):
    if request.method == "GET" and "generate" in request.GET:
        
        amount = request.GET.get("amount", "")
        invoice_number = request.GET.get("invoice_number", "")
        reference = request.GET.get("reference", "")
        category = request.GET.get("category", "")
        date = request.GET.get("date", "")
        print(amount, invoice_number, reference, category, date)

        expense_details = "Amount: 100\nInvoice Number: INV001\nReference: REF001\nCategory: Office Supplies\nDate: 2023-06-07"
        print(expense_details)

        description = create_assistant(expense_details)

        return render(request, "expenses/add-expenses.html", {"description": description, "values": request.GET})

    return render(request, "expenses/add-expenses.html")