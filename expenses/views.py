from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category, Expenses
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    categories = Category.objects.all()
    
    return render(request, 'expenses/index.html')

def add_expenses(request):
    if request.method == "GET":
        categories = Category.objects.all()
        context = {
            "categories": categories,
        }
        

    if request.method == "POST":
        amount = request.POST['amount']
            
        if not amount:
            messages.error(request, "Amount is required")
    
        
    return render(request, "expenses/add-expenses.html", context)


