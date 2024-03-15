from django.urls import path
from .views import RegistrationView, EmailValidationView, NameValidationView, PasswordValidationView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name='validate-email'),
    path('validate-name', csrf_exempt(NameValidationView.as_view()), name='validate-name'),
    path('validate-password', csrf_exempt(PasswordValidationView.as_view()), name='validate-password'),
]
