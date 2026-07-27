from typing import Literal

from ad.models import Ad
from contract.models import Contract
from .models import Customer


def update_ad(obj: Customer, method: Literal["add", "remove"]) -> None:
    """Обновление количества активных клиентов и профита рекламной компании"""
    if method not in ("add", "remove"):
        raise ValueError(f'Unknown method {method}')

    lead = obj.lead
    ad = lead.ad

    if method == "add":
        ad.customers_count += 1
    else:
        ad.customers_count -= 1

    Ad.update_profit(ad, Contract.get_sum_contracts(ad))

    ad.save()
