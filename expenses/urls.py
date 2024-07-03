"""
This module defines URL patterns for the Expenses application.

The `urlpatterns` list routes URLs to views. The available paths include:
- The root path and the "expenses/" path, both routed to the `index` view.
- The "add-expenses/" path, routed to the `add_expenses` view.
- The "edit-expense/<int:id>" path, routed to the `expense_edit` view.
- The "delete-expense/<int:id>" path, routed to the `delete_expense` view.
- The "generate_description/<int:id>/" path, routed to the
`generate_description` view.
- The "search_expenses/" path, routed to the `search_expenses` view, with CSRF
exemption.
"""


from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("", views.index, name="expenses"),
    path("expenses/", views.index, name="expenses"),
    path("add-expenses/", views.add_expenses, name="add-expenses"),
    path("edit-expense/<int:id>", views.expense_edit, name="expense-edit"),
    path("delete-expense/<int:id>", views.delete_expense,
         name="delete-expense"),
    path(
        "generate_description/<int:id>/",
        views.generate_description,
        name="generate-description",
    ),
    path(
        "search_expenses/", csrf_exempt(views.search_expenses),
        name="search-expenses"
    ),
]
