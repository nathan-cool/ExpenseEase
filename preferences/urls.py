from django.urls import path
from .views import PreferencesView

urlpatterns = [
    path('', PreferencesView, name='preferences'),
]