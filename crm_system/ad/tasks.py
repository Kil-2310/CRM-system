from celery import shared_task
from contract.models import Contract
from customer.models import Customer
from lead.models import Lead
from .models import Ad

from .utils import update_ad


@shared_task
def update_ad_profit(ad: Ad):
    update_ad(ad)


@shared_task
def recalculate_all_ads_statistics():
    for ad in Ad.objects.all():
        ad.leads_count = Lead.objects.filter(ad=ad).count()
        ad.customers_count = Customer.objects.filter(lead__ad=ad).count()
        Ad.update_profit(ad, Contract.get_sum_contracts(ad))
        ad.save()
