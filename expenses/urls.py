from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="expenses"),
    path("expenses/", views.index, name="expenses"),
    path("add-expenses/", views.add_expenses, name="add-expenses"),
    path("edit-expense/<int:id>", views.expense_edit, name="expense-edit"),
    path("delete-expense/<int:id>", views.delete_expense, name="delete-expense"),
]
