from django.db import models

from product.models import Product


class Contract(models.Model):
    """Модель контракта"""
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.IntegerField()
    file = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='contracts')

    def __str__(self) -> str:
        return f'Contract {self.name}'
