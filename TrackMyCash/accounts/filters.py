import django_filters
from .models import *
from django import forms
from django.forms import DateTimeInput
import datetime

class ExpenseFilter(django_filters.FilterSet):
    amount = django_filters.RangeFilter()


    class Meta:
        model = Expenses
        fields = ['transaction_type', 'account', 'category', 'date_added']
        widgets = {
            'transaction_type': forms.Select(attrs={'class': 'form-control equal-width'}),
            'account': forms.Select(attrs={'class': 'form-control equal-width'}),
            'category': forms.Select(attrs={'class': 'form-control equal-width'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control equal-width'}),
            'date_added': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control equal-width', 'value': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")}),
        }