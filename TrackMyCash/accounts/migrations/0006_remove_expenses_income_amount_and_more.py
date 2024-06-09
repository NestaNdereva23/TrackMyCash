# Generated by Django 5.0.6 on 2024-06-09 17:27

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_expenses_income_amount'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='income_amount',
        ),
        migrations.RemoveField(
            model_name='expenses',
            name='income_category',
        ),
        migrations.AlterField(
            model_name='expenses',
            name='transaction_type',
            field=models.CharField(choices=[('Expense', 'Expense'), ('Income', 'Income')], default='Expense', max_length=15),
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('Income', 'Income'), ('Expense', 'Expense')], default='Income', max_length=15)),
                ('account', models.CharField(choices=[('Mpesa', 'Mpesa'), ('Cash', 'Cash'), ('Bank', 'Bank'), ('Crypto', 'Crypto')], default='Cash', max_length=15)),
                ('income_category', models.CharField(choices=[('Salary', 'Salary'), ('PocketMoney', 'PocketMoney'), ('Investments', 'Investments'), ('Lotery', 'Lotery'), ('Grants', 'Grants'), ('Gifts', 'Gifts')], default='Salary', max_length=15)),
                ('income_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]