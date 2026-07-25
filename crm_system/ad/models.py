from django.db import models

from product.models import Product


class Ad(models.Model):
    """Модель рекламной компании"""
    name = models.CharField(max_length=255, unique=True)
    budget = models.IntegerField(blank=False, null=False)
    channel = models.CharField(max_length=255)
    leads_count = models.SmallIntegerField(default=0)
    customers_count = models.SmallIntegerField(default=0)
    profit = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Продукт продвижения в рекламной услуге
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')

    def __str__(self) -> str:
        return f'Ab {self.name}'
