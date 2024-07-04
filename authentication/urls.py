from django.urls import include, path
from .views import (
    RegistrationView,
    EmailValidationView,
    users_nameValidationView,
    PasswordValidationView,
    LoginView,
    LogoutView,
)
from django.views.decorators.csrf import csrf_exempt
from authentication import views

"""
URL configuration for the Authentication application.

This module defines the URL patterns for the authentication-related views,
including user registration, name validation, password
validation, account activation, login, logout, and social authentication.
"""

urlpatterns = [
    path("register", RegistrationView.as_view(), name="register"),
    path(
        "validate-email",
        csrf_exempt(EmailValidationView.as_view()),
        name="validate-email",
    ),
    path(
        "validate-name",
        csrf_exempt(users_nameValidationView.as_view()),
        name="validate-name",
    ),
    path(
        "validate-password",
        csrf_exempt(PasswordValidationView.as_view()),
        name="validate-password",
    ),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("accounts/", include("allauth.urls")),
    path("social_auth", views.social_auth, name="social_auth"),
]
