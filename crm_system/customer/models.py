from django.db import models


class Customer(models.Model):
    """Модель активного клиента"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
