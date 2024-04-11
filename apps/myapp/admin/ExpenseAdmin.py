from django.contrib import admin
from apps.myapp.models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass
