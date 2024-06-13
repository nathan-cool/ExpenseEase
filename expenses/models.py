from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Expenses(models.Model):
  amount = models.FloatField()  # The amount of the expense
  date = models.DateField(default=now)  # The date of the expense (default is the current date)
  description = models.TextField()  # The description of the expense
  owner = models.ForeignKey(to=User, on_delete=models.CASCADE)  # The owner of the expense (linked to a User)
  category = models.CharField(max_length=255)  # The category of the expense
  invoice_number = models.CharField(max_length=255, blank=True, null=True)  # The invoice number (optional)
  reference = models.CharField(max_length=255, blank=True, null=True)  # A reference for the expense (optional)

  def __str__(self):
    return self.category

  class Meta:
    ordering = ['-date']  # Ordering expenses by date in descending order


class Category(models.Model):
  name = models.CharField(max_length=255)  # The name of the category

  class Meta:
    verbose_name_plural = 'Categories'  # Plural name for the Category model

  def __str__(self):
    return self.name
