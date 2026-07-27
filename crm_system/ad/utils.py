from ad.models import Ad
from contract.models import Contract


def update_ad(obj: Ad) -> None:
    """Обновление количества активных клиентов и профита рекламной компании"""
    Ad.update_profit(obj, Contract.get_sum_contracts(obj))

    obj.save()
