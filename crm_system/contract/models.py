from typing import Union

from django.db import models
from django.db.models import Sum

from product.models import Product
from ad.models import Ad
from customer.models import Customer


class Contract(models.Model):
    """Модель контракта"""
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.IntegerField(default=0)
    file = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Услуга, на которую создается контракт
    product = models.ForeignKey(
        Product, null=True, on_delete=models.SET_NULL, related_name='contracts'
    )

    def __str__(self) -> str:
        return f'Contract {self.name}'

    @classmethod
    def get_sum_contracts(cls, ad: Ad) -> Union[int, float]:
        """Получение суммы контрактов по конкретной рекламной компании"""
        return Customer.objects.filter(lead__ad=ad).aggregate(
            total=Sum('contract__cost')
        )['total'] or 0
