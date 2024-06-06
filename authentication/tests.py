from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class AddExpensesViewTest(TestCase):

    def setUp(self):
        # Set up a test client
        self.client = Client()

        # Create a test user and log them in
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        # Create some test categories
        self.category1 = Category.objects.create(name="Food")
        self.category2 = Category.objects.create(name="Rent")

    def test_get_add_expenses_view(self):
        # Test GET request
        response = self.client.get(reverse("add_expenses"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "expenses/add-expenses.html")
        self.assertIn("categories", response.context)

    def test_post_add_expenses_missing_fields(self):
        # Test POST request with missing fields
        response = self.client.post(
            reverse("add_expenses"),
            {
                "amount": "",
                "date": "",
                "category": "",
                "description": "",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "expenses/add-expenses.html")
        self.assertContains(response, "Amount is required")
        self.assertContains(response, "Date is required")
        self.assertContains(response, "Category is required")
        self.assertContains(response, "Description is required")

    def test_post_add_expenses_successful(self):
        # Test POST request with all fields filled
        response = self.client.post(
            reverse("add_expenses"),
            {
                "amount": "100",
                "date": "2023-01-01",
                "category": self.category1.id,
                "description": "Groceries",
                "invoice_number": "INV123",
                "reference": "REF123",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("expenses"))
        self.assertEqual(Expenses.objects.count(), 1)

        expense = Expenses.objects.first()
        self.assertEqual(expense.amount, "100")
        self.assertEqual(expense.date, "2023-01-01")
        self.assertEqual(expense.category, self.category1)
        self.assertEqual(expense.description, "Groceries")
        self.assertEqual(expense.invoice_number, "INV123")
        self.assertEqual(expense.reference, "REF123")
