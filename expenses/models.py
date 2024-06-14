from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Expenses(models.Model):
    """
    Model representing expenses
    """

    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    invoice_number = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        """
        String representation of the expense object
        """
        return self.category

    class Meta:
        """
        Meta class to define ordering of expenses by date
        """

        ordering = ["-date"]


class Category(models.Model):
    """
    Model representing categories
    """

    name = models.CharField(max_length=255)

    class Meta:
        """
        Meta class to define the plural name for the category model
        """

        verbose_name_plural = "Categories"

    def __str__(self):
        """
        String representation of the category object
        """
        return self.name
