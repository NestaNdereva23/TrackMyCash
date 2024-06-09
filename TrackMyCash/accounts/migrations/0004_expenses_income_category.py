# Generated by Django 5.0.6 on 2024-06-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_expenses_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='income_category',
            field=models.CharField(choices=[('Salary', 'Salary'), ('PocketMoney', 'PocketMoney'), ('Investments', 'Investments'), ('Lotery', 'Lotery'), ('Grants', 'Grants'), ('Gifts', 'Gifts')], default='Salary', max_length=15),
        ),
    ]