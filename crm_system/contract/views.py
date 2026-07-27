from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Contract
from .utils import update_ad


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
        update_ad(self.object)
        return response


class ContractDeleteView(PermissionRequiredMixin, DeleteView):
    """Удаление контракта"""
    permission_required = 'contract.delete_contract'

    queryset = Contract.objects.all().defer('created_at', 'updated_at')
    template_name = 'contract/contracts-delete.html'

    success_url = reverse_lazy('contract:contract_list')
