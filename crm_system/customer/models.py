from django.db import models

from lead.models import Lead


class Customer(models.Model):
    """Модель активного клиента"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    lead = models.OneToOneField(Lead, on_delete=models.CASCADE, related_name='customer')

    def __str__(self) -> str:
        return f'Customer {self.lead.first_name} {self.lead.last_name}'
