from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Expenses, Income, Transfer
from django.forms import ModelForm, DateTimeInput
import datetime
from django.core.exceptions import ValidationError

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

#user expensesform
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
            'date_added': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control equal-width', 'value': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")}),
        }
        def clean_date_added(self):
            date = self.cleaned_data.get('date_added')
            if date and date.date() > datetime.date.today():
                raise ValidationError("The date cannot be in the future.")
            return date

#form for handling all income
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
            'date_added': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control equal-width', 'value': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")}),
        }
        def clean_date_added(self):
            date = self.cleaned_data['date_added']
            if date > datetime.date.today():  # 🖘 raise error if greater than
                raise forms.ValidationError(" invalid date!")
            return date

class TransferForm(ModelForm):
    class Meta:
        model = Transfer
        fields = ['transaction_type', 'from_account', 'to_account', 'amount', 'description', 'date_added' ]
        widgets = {
            'transaction_type': forms.Select(attrs={'class': 'form-control equal-width'},),
            'from_account': forms.Select(attrs={'class': 'form-control equal-width'}),
            'to_account': forms.Select(attrs={'class': 'form-control equal-width'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control equal-width'}),
            'description': forms.TextInput(attrs={'class': 'form-control equal-width'}),
            'date_added': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control equal-width', 'value': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")}),
        }
        def clean_date_added(self):
            date = self.cleaned_data['date_added']
            if date > datetime.date.today():  # 🖘 raise error if greater than
                raise forms.ValidationError(" invalid date!")
            return date