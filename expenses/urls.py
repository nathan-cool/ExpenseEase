from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='expenses'),
    path('add-expenses', views.index, name='add-expenses')
    
]
