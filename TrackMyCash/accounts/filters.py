import django_filters
from .models import *

class ExpenseFilter(django_filters.FilterSet):
    class Meta:
        model = Expenses
        fields = ['transaction_type', 'account', 'category', 'date_added']