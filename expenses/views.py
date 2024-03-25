from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    return render(request, 'expenses/index.html')
  
def add_expenses(request):
    return render(request, 'expenses/add-expenses.html')