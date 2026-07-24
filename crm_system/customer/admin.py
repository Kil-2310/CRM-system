from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Модель админки для активного клиента"""
    list_display = ('id', 'lead__first_name', 'lead__last_name',)
