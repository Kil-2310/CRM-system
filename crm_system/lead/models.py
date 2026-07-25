from django.db import models

from ad.models import Ad


class Lead(models.Model):
    """Модель потенциального клиента"""
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Рекламная услуга, из которой пришел потенциальный клиент
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='leads')

    def __str__(self) -> str:
        return f'Lead {self.last_name} {self.first_name}'
