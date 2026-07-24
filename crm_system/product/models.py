from django.db import models


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Product {self.name}'
