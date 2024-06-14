from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Expenses, Income
from django.forms import ModelForm, DateTimeInput

# User login form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("error")
        return email


class ExpenseForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['transaction_type', 'account', 'category', 'amount', 'description', 'date_added' ]
        widgets = {
            'transaction_type': forms.Select(attrs={'class': 'form-control equal-width'}),
            'account': forms.Select(attrs={'class': 'form-control equal-width'}),
            'category': forms.Select(attrs={'class': 'form-control equal-width'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control equal-width'}),
            'description': forms.TextInput(attrs={'class': 'form-control equal-width'}),
            'date_added': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control equal-width'}),
        }

class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ['transaction_type', 'account', 'category', 'amount', 'description', 'date_added' ]
        widgets = {
            'transaction_type': forms.Select(attrs={'class': 'form-control equal-width'},),
            'account': forms.Select(attrs={'class': 'form-control equal-width'}),
            'category': forms.Select(attrs={'class': 'form-control equal-width'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control equal-width'}),
            'description': forms.TextInput(attrs={'class': 'form-control equal-width'}),
            'date_added': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control equal-width'}),
        }