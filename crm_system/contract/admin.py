from django.contrib import admin

from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """Модель админки для контракта"""
    list_display = ('name', 'start_date', 'end_date')
