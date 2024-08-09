from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Expenses)
admin.site.register(Income)
admin.site.register(Transfer)
admin.site.register(AccountBalance)