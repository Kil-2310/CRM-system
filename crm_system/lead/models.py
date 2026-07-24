from django.db import models


class Lead(models.Model):
    """Модель потенциального клиента"""
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Lead {self.last_name} {self.first_name}'
