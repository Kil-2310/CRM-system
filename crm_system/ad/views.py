from decimal import Decimal

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Sum

from .models import Ad
from customer.models import Customer


class AdListView(PermissionRequiredMixin, ListView):
    """Список рекламных компаний"""
    permission_required = 'ad.view_ad'

    queryset = Ad.objects.all().only('name', 'budget', 'channel', 'product')
    template_name = "ad/ads-list.html"
    context_object_name = 'ads'


class AdDetailView(PermissionRequiredMixin, DetailView):
    """Детали рекламной компании"""
    permission_required = 'ad.view_ad'

    queryset = Ad.objects.all().only('name', 'budget', 'channel', 'product')
    template_name = "ad/ads-detail.html"


class AdCreateView(PermissionRequiredMixin, CreateView):
    """Создание рекламной компании"""
    permission_required = 'ad.add_ad'

    queryset = Ad.objects.all().only('name', 'budget', 'channel', 'product')
    template_name = "ad/ads-create.html"
    fields = 'name', 'budget', 'channel', 'product'

    success_url = reverse_lazy('ad:ad_list')


class AdUpdateView(PermissionRequiredMixin, UpdateView):
    """Обновление рекламной компании"""
    permission_required = 'ad.change_ad'

    queryset = Ad.objects.all().only('name', 'budget', 'channel', 'product')
    template_name = "ad/ads-edit.html"
    fields = 'name', 'budget', 'channel', 'product'

    success_url = reverse_lazy('ad:ad_list')

    def form_valid(self, form):
        response = super().form_valid(form)

        sum_contracts = Customer.objects.filter(
            lead__ad=self.object
        ).aggregate(
            total=Sum('contract__cost')
        )['total']

        if sum_contracts == 0:
            self.object.profit = 0
        else:
            self.object.profit = round(Decimal(str(sum_contracts)) / Decimal(str(self.object.budget)), 2)

        self.object.save()
        return response


class AdDeleteView(PermissionRequiredMixin, DeleteView):
    """Удаление рекламной компании"""
    permission_required = 'ad.delete_ad'

    queryset = Ad.objects.all().only('name', 'budget', 'channel', 'product')
    template_name = "ad/ads-delete.html"

    success_url = reverse_lazy('ad:ad_list')


class AdStatisticView(PermissionRequiredMixin, ListView):
    """Получение статистики рекламных компаний"""
    permission_required = 'ad.view_ad'

    queryset = Ad.objects.all().defer('created_at', 'updated_at')
    template_name = "ad/ads-statistic.html"
    context_object_name = 'ads'
