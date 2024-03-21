from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
import re
from django.contrib import messages



# Create your views here.

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    
    def post(self, request):
        #messages.success(request, 'success')
        #messages.warning(request, 'warning')
        #messages.info(request, "info")
        #messages.error(request, 'error')
        name = request.POST['users_name']
        email = request.POST['email']
        password = request.POST['password']
        
        context={
            'fieldValues': request.POST
        }
        
        if not User.objects.filter(email=email).exists():
            if len(password)<6:
                messages.error(request,"Password too short")
                return render(request, 'authentication/register.html', context)
                
            user = User.objects.create_user(username = email, first_name=name, email=email)
            user.set_password(password)
            user.save()
            messages.success(request,"Verification email sent")

        return render(request, 'authentication/register.html')

    
class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        
        # Check if email is empty
        if not str(email).strip():
            return JsonResponse({'email_error': 'Email cannot be empty'}, status=400)
        
        # Check if email is already in use
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry, this email is already in use'}, status=409)
        
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        
        # Check if email has valid format
        if not re.match(email_regex, email):
            return JsonResponse({'email_error': 'Invalid email format'}, status=400)
        
        
        return JsonResponse({'email_valid': True})
    
    
class users_nameValidationView(View):
    def post(self, request):
        users_name_regex = r'^[A-Za-z\s]+$'
        data = json.loads(request.body)
        users_name = data['users_name']
        
        # Check if users_name is empty
        if not str(users_name).strip():
            return JsonResponse({'users_name_error': 'users_name cannot be empty'}, status=400)
        
        # Check if users_name contains only letters and spaces
        if not re.match(users_name_regex, users_name):
            return JsonResponse({'users_name_error': 'Name can only contain letters and spaces'}, status=400)
        
        return JsonResponse({'users_name_valid': True})
    
class PasswordValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        password = data['password']
        password_regex = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$'
        
        # Check if password is at least 8 characters long
        if len(str(password).strip()) < 8:
            return JsonResponse({'password_error': 'Password must be at least 8 characters long'}, status=400)
    
        # Check if password contains at least one uppercase letter, one lowercase letter, and one number
        if not re.match(password_regex, password):
            return JsonResponse({'password_error': 'Password must contain at least one uppercase letter, one lowercase letter, and one number'}, status=400)
        
        return JsonResponse({'password_valid': True})
