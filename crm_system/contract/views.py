from decimal import Decimal

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Sum

from .models import Contract
from ad.models import Ad
from customer.models import Customer


class ContractListView(PermissionRequiredMixin, ListView):
    """Список всех контрактов"""
    permission_required = 'contract.view_contract'

    queryset = Contract.objects.all().defer('created_at', 'updated_at')
    template_name = 'contract/contracts-list.html'
    context_object_name = 'contracts'


class ContractDetailView(PermissionRequiredMixin, DetailView):
    """Детали контракта"""
    permission_required = 'contract.view_contract'

    queryset = Contract.objects.select_related('product').all().defer('created_at', 'updated_at')
    template_name = 'contract/contracts-detail.html'


class ContractCreateView(PermissionRequiredMixin, CreateView):
    """Создание контракта"""
    permission_required = 'contract.add_contract'

    queryset = Contract.objects.all().defer('created_at', 'updated_at')
    template_name = 'contract/contracts-create.html'
    fields = 'name', 'start_date', 'end_date', 'cost', 'product', 'file'

    success_url = reverse_lazy('contract:contract_list')


class ContractUpdateView(PermissionRequiredMixin, UpdateView):
    """Обновление статистики рекламной компании при обновлении контракта"""
    permission_required = 'contract.change_contract'

    queryset = Contract.objects.all().defer('created_at', 'updated_at').select_related('product')
    template_name = 'contract/contracts-edit.html'
    fields = 'name', 'start_date', 'end_date', 'cost', 'product', 'file'

    success_url = reverse_lazy('contract:contract_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        ad = Ad.objects.get(product=self.product)

        sum_contracts = Customer.objects.filter(
            lead__ad=ad
        ).aggregate(
            total=Sum('contract__cost')
        )['total']

        if sum_contracts == 0:
            ad.profit = 0
        else:
            ad.profit = round(Decimal(str(sum_contracts)) / Decimal(str(ad.budget)), 2)

        ad.save()
        return response


class ContractDeleteView(PermissionRequiredMixin, DeleteView):
    """Удаление контракта"""
    permission_required = 'contract.delete_contract'

    queryset = Contract.objects.all().defer('created_at', 'updated_at')
    template_name = 'contract/contracts-delete.html'

    success_url = reverse_lazy('contract:contract_list')
