from ad.models import Ad
from .models import Contract


def update_ad(obj: Contract) -> None:
    """Обновление количества активных клиентов и профита рекламной компании"""
    ad = Ad.objects.get(product=obj.product)
    Ad.update_profit(ad, Contract.get_sum_contracts(ad))

    ad.save()
