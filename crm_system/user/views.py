from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from lead.models import Lead
from product.models import Product
from customer.models import Customer


class ApplicationMetricsListView(LoginRequiredMixin, TemplateView):
    """Получение общих метрик приложения"""
    template_name = 'user/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['products_count'] = Product.objects.count()
        context['advertisements_count'] = 10 # TODO: не забыть изменить заглушку
        context['leads_count'] = Lead.objects.count()
        context['customers_count'] = Customer.objects.count()

        return context
