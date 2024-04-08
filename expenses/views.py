from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category, Expenses


# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    category = Category.objects.all()
    
    return render(request, 'expenses/index.html')

def add_expenses(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, "expenses/add-expenses.html", context)
