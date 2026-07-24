from django.views.generic import TemplateView
from django.db.models import Count

from lead.models import Lead
from product.models import Product
from customer.models import Customer


class ApplicationMetricsListView(TemplateView):
    """Получение общих метрик приложения"""
    template_name = 'user/index.html'
