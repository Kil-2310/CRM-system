from django.db import models

from lead.models import Lead
from contract.models import Contract


class Customer(models.Model):
    """Модель активного клиента"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # После заключения контракта потенциальный клиент переходит в статус активного клиента
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE, related_name='customer')
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='customer')

    def __str__(self) -> str:
        return f'Customer {self.lead.first_name} {self.lead.last_name}'
