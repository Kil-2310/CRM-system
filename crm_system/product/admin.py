from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Модель админки для товаров"""
    list_display = ('id', 'name', 'description', 'cost')
