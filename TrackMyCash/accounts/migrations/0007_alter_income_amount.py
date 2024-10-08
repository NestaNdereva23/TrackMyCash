# Generated by Django 5.1 on 2024-09-24 21:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_accountbalance_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
