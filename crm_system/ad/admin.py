from django.contrib import admin

from .models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """Админка для рекламной компании"""
    list_display = ('name', 'created_at')
