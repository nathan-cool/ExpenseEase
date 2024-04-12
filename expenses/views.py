from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Category, Expenses
from django.shortcuts import redirect
from django.contrib import messages
import openai


# Create your views here.
@login_required(login_url="/authentication/login")
def index(request):
    categories = Category.objects.all()
    expenses = Expenses.objects.filter(owner=request.user)

    context = {
        "expenses": expenses,
    }

    return render(request, "expenses/index.html", context)


def add_expenses(request):
    categories = Category.objects.all()
    context = {"categories": categories, "values": request.POST}

    if request.method == "GET":
        return render(request, "expenses/add-expenses.html", context)

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


def expense_edit(request, id):

    expense = Expenses.objects.get(pk=id)

    context = {
        "expense": expense,
        "invoice_number": expense.invoice_number,
        "reference": expense.reference,
        "amount": expense.amount,
        "category": expense.category,
        "date": expense.date,
        "description": expense.description,
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
        return redirect("expenses")

    else:
        messages.info(request, "Expense not edited")
        return render(request, "expenses/edit-expense.html", context)


def delete_expense(request, id):
    if request.method == "GET":

        expense = Expenses.objects.get(pk=id)
        expense.delete()
        messages.success(request, "Expense deleted successfully")
        return redirect("expenses")


openai.api_key = "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"


def create_assistant(expense_details):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Generate a description for this expense based on the provided details"},
                {"role": "user", "content": f"Amount: {expense_details['amount']}\nInvoice Number: {expense_details['invoice_number']}\nReference: {expense_details['reference']}\nCategory: {expense_details['category']}\nDate: {expense_details['date']}"}
            ]
        )
        print("API Response:", response)  # Print the API response
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error: {str(e)}")
        return "An error occurred while generating the description."

def generate_description(request, id):
    expense = get_object_or_404(Expenses, pk=id)
    expense_details = {
        'amount': expense.amount,
        'invoice_number': expense.invoice_number,
        'reference': expense.reference,
        'category': expense.category, 
        'date': expense.date.strftime("%Y-%m-%d"),  
    }
    generated_description = create_assistant(expense_details)
    invoice_number = expense.invoice_number
    
    context = {
        "description": generated_description,
        "expense": expense,
        "invoice_number": invoice_number,
        "reference": expense.reference,
        "amount": expense.amount,
        "category": expense.category,
        "date": expense.date,
    }
    
    if request.method == "GET":
        return render(request, "expenses/edit-expense.html", context)
    
 