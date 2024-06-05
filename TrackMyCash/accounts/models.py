
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

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(default=timezone.now)
    expense_category = models.CharField(max_length=15, choices=EXPENSE_CATEGORY, default="Car")

    # def __str__(self):
        # return f"{self.user.username}'s expense on {self.date_added.strftime('%Y-%m-%d')}"


    
    # def date_added(self):
    #     publication=timezone.now()
    #     self.save()






# initial_amount =
# expense_amount=
# income_amount=
# dateadded=
# type_of_expense=
# type_of_income=
# current_balance=


