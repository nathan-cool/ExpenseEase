# Generated by Django 5.0.3 on 2024-03-29 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0002_rename_currency_userpreferences_currencies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpreferences',
            old_name='currencies',
            new_name='currency',
        ),
    ]
