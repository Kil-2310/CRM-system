from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    """Модель админки для потенциального клиента"""
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone')
