# Standard library imports
import json
import re
from django.shortcuts import redirect, render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .utils import token_generator
from django.views import View


class RegistrationView(View):
    def splitName(self, name):
        
        parts = name.split(' ', 1)
        
        first_name = parts[0]
        last_name = parts[1] if len(parts) > 1 else '' 
        
        return first_name, last_name

    def get(self, request):
        return render(request, 'authentication/register.html')
    
    def post(self, request):
        
        name = request.POST['users_name']
        first_name, last_name = self.splitName(name)
        
        password = request.POST['password']
        email = request.POST['email']
        context={
            'fieldValues': request.POST
        }
        
        if not User.objects.filter(email=email).exists():
            if len(password)<6:
                messages.error(request,"Invalid password")
                return render(request, 'authentication/register.html', context)
            if not re.match(r'^[A-Za-z\s]+$', name):
                messages.error(request,"Invalid name")
                return render(request, 'authentication/register.html', context)
            if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                messages.error(request,"Invalid email")
                return render(request, 'authentication/register.html', context)
            if User.objects.filter(email=email).exists():
                messages.error(request,"Email already exists")
                return render(request, 'authentication/register.html', context)
            
            def send_verification_email(user):
                try:
                    domain = get_current_site(request).domain
                    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                    link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token_generator.make_token(user)})
                    activate_url = 'http://' + domain + link
                    email_subject = "Activate your expenses account"
                    email_body = "Hi " + name + "! Please use this link to verify your account\n" + activate_url
                    send_email = EmailMessage(email_subject, email_body, 'MS_Wj5pnF@trial-x2p0347y5d34zdrn.mlsender.net', [email],)
                    send_email.send(fail_silently=False)
                    messages.success(request, "Verification email sent")
                except Exception as e:
                    messages.error(request, "An error occurred while sending the email")
                    pass
            
        
            user = User.objects.create_user(email = email, first_name=first_name, last_name= last_name, username=email)
            user.set_password(password)
            user.is_active=False
            user.save()
            send_verification_email(user)
            
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
    
    
class VerificationView(View):
    
    def get(self, request, uidb64, token):
        
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)
            
            if not token_generator.check_token(user, token):
                return redirect('login'+ '?message='+'User already activated')
            
            if user.is_active:
                return redirect('login'+ '?message='+'User already activated')
            
            user.is_active = True
            user.save()
            
            successMessage = messages.success(request, 'Account activated successfully')
            
            return redirect('login'+ '?message='+successMessage)
            
            
            
        except Exception as e:
            pass
       
      
        return redirect('login')
    
    
class LoginView(View):    
    def get(self, request):
        return render(request, 'authentication/login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            user = authenticate(request, username=email, password=password)

        try:
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, f'Welcome, {user.first_name}!')
                    return redirect('add-expenses')
                else:
                    messages.error(request, 'Account is not activated')
            else: 
                messages.error(request, 'Invalid login credentials')
        except Exception as e:
            pass
        else: 
            messages.error(request, 'Please fill in all fields')
    
        return render(request, 'authentication/login.html')
    
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('login')
    