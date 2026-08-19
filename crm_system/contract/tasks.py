from celery import shared_task
from .models import Contract
from django.utils import timezone

import logging


logger = logging.getLogger(__name__)

@shared_task
def check_expired_contracts():
    contracts = Contract.objects.filter(end_date__lt = timezone.now().date())
    count = contracts.count()

    logger.info('Найдено истекших контрактов: %s', count)

    for contract in contracts:
        logger.info(
            'Контракт %s id = %s истек %s',
            contract.name,
            contract.pk,
            contract.end_date
        )
