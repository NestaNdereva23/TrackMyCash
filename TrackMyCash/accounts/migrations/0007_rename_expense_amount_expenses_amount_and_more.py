# Generated by Django 5.0.6 on 2024-06-09 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_expenses_income_amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenses',
            old_name='expense_amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='expenses',
            old_name='expense_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='income_amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='income_category',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='expenses',
            name='transaction_type',
            field=models.CharField(choices=[('Expense', 'Expense')], default='Expense', max_length=15),
        ),
        migrations.AlterField(
            model_name='income',
            name='transaction_type',
            field=models.CharField(choices=[('Income', 'Income')], default='Income', max_length=15),
        ),
    ]