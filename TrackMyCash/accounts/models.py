
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Expenses(models.Model):
    EXPENSE_CATEGORY = [
        ("Car", "Car"),
        ("Bills", "Bills"),
        ("Education", "Education"),
        ("Health", "Health"),
        ("Shopping", "Shopping"),
        ("Transport", "Transport"),
        ("WiFi", "WiFi"),
    ]

    TRANSACTION_TYPE = [
        ("Expense", "Expense"),
    ]

    ACCOUNT_CATEGORY = [
        ("Mpesa", "Mpesa"),
        ("Cash", "Cash"),
        ("Bank", "Bank"),
        ("Crypto", "Crypto"),

    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE, default="Expense", )
    account = models.CharField(max_length=15, choices=ACCOUNT_CATEGORY, default="Cash")
    category = models.CharField(max_length=15, choices=EXPENSE_CATEGORY, default="Car")    
    description = models.CharField(max_length=1000, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(default=timezone.now)

    #ordering transactions
    class Meta:
        ordering = ['-date_added']
        # indexes = [models.Index(fields=['-date_added']), ]

class Income(models.Model):
    TRANSACTION_TYPE = [
        ("Income", "Income"),
    ]
    INCOME_CATEGORY = [
        ("Salary", "Salary"),
        ("PocketMoney", "PocketMoney"),
        ("Investments", "Investments"),
        ("Lotery", "Lotery"),
        ("Grants", "Grants"),
        ("Gifts", "Gifts"),
    ]
    ACCOUNT_CATEGORY = [
        ("Mpesa", "Mpesa"),
        ("Cash", "Cash"),
        ("Bank", "Bank"),
        ("Crypto", "Crypto"),

    ]
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE, default="Income")
    account = models.CharField(max_length=15, choices=ACCOUNT_CATEGORY, default="Cash")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.CharField(max_length=15, choices=INCOME_CATEGORY, default="Salary")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.CharField(max_length=1000, blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_added']
        # indexes = [models.Index(fields=['-date_added']), ]
    
class Transfer(models.Model):
    TRANSACTION_TYPE = [
        ("Transfer", "Transfer"),
    ]
    ACCOUNT_CATEGORY = [
        ("Mpesa", "Mpesa"),
        ("Cash", "Cash"),
        ("Bank", "Bank"),
        ("Crypto", "Crypto"),

    ]
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE, default="Income")
    from_account = models.CharField(max_length=15, choices=ACCOUNT_CATEGORY, default="Mpesa")
    to_account = models.CharField(max_length=15, choices=ACCOUNT_CATEGORY, default="Cash")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.CharField(max_length=1000, blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_added']
        # indexes = [models.Index(fields=['-date_added']), ]

















