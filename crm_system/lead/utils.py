from typing import Literal

from .models import Lead


def update_ad(obj: Lead, method: Literal['add', 'remove']) -> None:
    """Обновление количества лидов в рекламной компании"""
    if method not in ('add', 'remove'):
        raise ValueError(f'Unknown method {method}')

    ad = obj.ad

    if method == 'add':
        ad.leads_count += 1
    else:
        ad.leads_count -= 1

    ad.save()
