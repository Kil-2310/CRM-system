from django.db import models

from product.models import Product


class Ad(models.Model):
    """Модель рекламной компании"""
    name = models.CharField(max_length=255)
    budget = models.IntegerField()
    channel = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Ab {self.name}'
