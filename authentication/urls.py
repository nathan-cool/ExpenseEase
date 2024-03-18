from django.urls import path
from .views import RegistrationView, EmailValidationView, users_nameValidationView, PasswordValidationView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name='validate-email'),
    path('validate-name', csrf_exempt(users_nameValidationView.as_view()), name='validate-name'),
    path('validate-password', csrf_exempt(PasswordValidationView.as_view()), name='validate-password'),
]
