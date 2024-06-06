from django.urls import include, path
from .views import RegistrationView, EmailValidationView, users_nameValidationView, PasswordValidationView, VerificationView, LoginView, LogoutView, social_auth
from django.views.decorators.csrf import csrf_exempt
from authentication import views



urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name='validate-email'),
    path('validate-name', csrf_exempt(users_nameValidationView.as_view()), name='validate-name'),
    path('validate-password', csrf_exempt(PasswordValidationView.as_view()), name='validate-password'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('accounts/', include('allauth.urls')),
    path('social_auth', views.social_auth, name='social_auth'),
]
