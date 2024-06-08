from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Expenses
from django.forms import ModelForm, DateTimeInput

# User login form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]

class ExpenseForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['transaction_type', 'account', 'expense_category', 'expense_amount', 'description', 'date_added' ]
        widgets = {
            'transaction_type': forms.Select(attrs={'class': 'form-control equal-width'}),
            'account': forms.Select(attrs={'class': 'form-control equal-width'}),
            'expense_category': forms.Select(attrs={'class': 'form-control equal-width'}),
            'expense_amount': forms.NumberInput(attrs={'class': 'form-control equal-width'}),
            'description': forms.TextInput(attrs={'class': 'form-control equal-width'}),
            'date_added': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control equal-width'}),
        }
