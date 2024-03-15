from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
import re


# Create your views here.

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    
class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        
        if not str(email).strip():
            return JsonResponse({'email_error': 'Email cannot be empty'}, status=400)
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry, this email is already in use'}, status=409)
        
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            return JsonResponse({'email_error': 'Invalid email format'}, status=400)
        
        return JsonResponse({'email_valid': True})
    
    
class NameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        name = data['name']
        
        if not str(name).strip():
            return JsonResponse({'name_error': 'name cannot be empty'}, status=400)
        
        return JsonResponse({'name_valid': True})
    
class PasswordValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        password = data['password']
        password_regex = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$'
        
        if len(str(password).strip()) < 8:
            return JsonResponse({'password_error': 'Password must be at least 8 characters long'}, status=400)
    
        if  not re.match(password_regex, password):
            return JsonResponse({'password_error': 'Password must contain at least one uppercase letter, one lowercase letter and one number'}, status=400)
        
        return JsonResponse({'password_valid': True})

    
    
    
    