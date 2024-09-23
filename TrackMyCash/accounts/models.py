
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

ACCOUNT_CATEGORY = [
        ("Mpesa", "Mpesa"),
        ("AirtelMoney", "AirtelMoney"),
        ("Cash", "Cash"),
        ("Bank", "Bank"),
        ("CryptoWallet", "CryptoWallet"),
        ("Savings", "Savings"),
        ("MoneyMarketFund", "MoneyMarketFund"),
        ("PayPal", "PayPal"),
        ("Other", "Other")

]

class Expenses(models.Model):
    EXPENSE_CATEGORY = [
        ("CarBills", "CarBills"),
        ("Subscriptions", "Subscriptions"),
        ("Bills/Utilities", "Bills/Utilities"),
        ("Morgage/Rent", "Morgage/Rent"),
        ("Education", "Education"),
        ("MedicalCare", "MedicalCare"),
        ("LoanPayments", "LoanPayments"),
        ("Shopping", "Shopping"),
        ("Transport", "Transport"),
        ("WiFi", "WiFi"),
        ("Clothing", "Clothing"),
        ("Others", "Others"),

    ]

    TRANSACTION_TYPE = [
        ("Expense", "Expense"),
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


    def __str__(self) -> str:
        return self.transaction_type

class Income(models.Model):
    TRANSACTION_TYPE = [
        ("Income", "Income"),
    ]
    INCOME_CATEGORY = [
        ("Salary", "Salary"),
        ("PocketMoney/Allowance", "PocketMoney/Allowance"),
        ("Investments", "Investments"),
        ("Lotery", "Lotery"),
        ("Grants", "Grants"),
        ("Gifts", "Gifts"),
        ("RentalIncome", "RentalIncome"),

    ]

    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE, default="Income")
    account = models.CharField(max_length=15, choices=ACCOUNT_CATEGORY, default="Cash")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.CharField(max_length=30, choices=INCOME_CATEGORY, default="Salary")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.CharField(max_length=1000, blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_added']
        # indexes = [models.Index(fields=['-date_added']), ]

    def __str__(self) -> str:
        return f'{self.transaction_type} + {self.category}'
    
class Transfer(models.Model):
    TRANSACTION_TYPE = [
        ("Transfer", "Transfer"),
    ]
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE, default="Transfer")
    from_account = models.CharField(max_length=15, choices=ACCOUNT_CATEGORY, default="Mpesa")
    to_account = models.CharField(max_length=15, choices=ACCOUNT_CATEGORY, default="Cash")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.CharField(max_length=1000, blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_added']
        # indexes = [models.Index(fields=['-date_added']), ]

    def __str__(self) -> str:
        return {self.transaction_type}



class AccountBalance(models.Model):
    account = models.CharField(max_length=15, choices=ACCOUNT_CATEGORY, default="Cash")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startingbalance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    last_updated = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['account', 'user']

    def __str__(self) -> str:
        return self.account

# class UserProfile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
#     startingbalance = models.DecimalField(max_digits=90, decimal_places=2, default=0)
#     denomination = models.CharField(max_length=255)












