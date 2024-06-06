from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("", views.index, name="expenses"),
    path("expenses/", views.index, name="expenses"),
    path("add-expenses/", views.add_expenses, name="add-expenses"),
    path("edit-expense/<int:id>", views.expense_edit, name="expense-edit"),
    path("delete-expense/<int:id>", views.delete_expense, name="delete-expense"),
    path("generate_description/<int:id>/", views.generate_description, name="generate-description"),
    path("search_expenses/", csrf_exempt( views.search_expenses), name="search-expenses"),
]
