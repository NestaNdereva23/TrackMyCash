from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Expenses
from django.forms import ModelForm, DateTimeInput


#userlogin form

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]


class ExpenseForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['expense_amount', 'date_added', 'expense_category']
        widgets = {
            'date_added': DateTimeInput(attrs={'type': 'datetime-local'}),
        }