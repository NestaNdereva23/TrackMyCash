
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
        ("Income", "Income"),
        ("Transfer", "Transfer"),

    ]

    ACCOUNT_CATEGORY = [
        ("Mpesa", "Mpesa"),
        ("Cash", "Cash"),
        ("Bank", "Bank"),
        ("Crypto", "Crypto"),

    ]

    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE, default="Expense")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    account = models.CharField(max_length=15, choices=ACCOUNT_CATEGORY, default="Cash")
    expense_category = models.CharField(max_length=15, choices=EXPENSE_CATEGORY, default="Car")
    description = models.CharField(max_length=1000, blank=True, null=True)
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(default=timezone.now)

    #ordering transactions
    class Meta:
        ordering = ['-date_added']
        # indexes = [models.Index(fields=['-date_added']), ]


     
   
    # def __str__(self):
        # return f"{self.user.username}'s expense on {self.date_added.strftime('%Y-%m-%d')}"












