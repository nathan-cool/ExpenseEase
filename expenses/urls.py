from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='expenses'),  # URL pattern for the expenses page
    path('add-expenses', views.index, name='add-expenses'),

    # URL pattern for adding expenses
]
