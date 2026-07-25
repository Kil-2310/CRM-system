from decimal import Decimal

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Sum

from .models import Ad
from customer.models import Customer


class AdListView(LoginRequiredMixin, ListView):
    """Список рекламных компаний"""
    queryset = Ad.objects.all().only('name', 'budget', 'channel', 'product')
    template_name = "ad/ads-list.html"
    context_object_name = 'ads'


class AdDetailView(LoginRequiredMixin, DetailView):
    """Детали рекламной компании"""
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
            lead__ad=self
        ).aggregate(
            total=Sum('contract__cost')
        )['total']

        if sum_contracts == 0:
            self.profit = 0
        else:
            self.profit = round(Decimal(str(sum_contracts)) / Decimal(str(self.budget)), 2)

        self.save()
        return response


class AdDeleteView(PermissionRequiredMixin, DeleteView):
    """Удаление рекламной компании"""
    permission_required = 'ad.delete_ad'

    queryset = Ad.objects.all().only('name', 'budget', 'channel', 'product')
    template_name = "ad/ads-delete.html"

    success_url = reverse_lazy('ad:ad_list')


class AdStatisticView(LoginRequiredMixin, ListView):
    """Получение статистики рекламных компаний"""
    queryset = Ad.objects.all().defer('created_at', 'updated_at')
    template_name = "ad/ads-statistic.html"
    context_object_name = 'ads'
