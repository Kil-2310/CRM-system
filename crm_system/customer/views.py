from decimal import Decimal

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Sum

from .models import Customer


class CustomerList(PermissionRequiredMixin, ListView):
    """Список активных клиентов"""
    permission_required = "customer.view_customer"

    queryset = Customer.objects.all().defer('created_at', 'updated_at')
    template_name = 'customer/customers-list.html'
    context_object_name = 'customers'


class CustomerDetail(PermissionRequiredMixin, DetailView):
    """Детали активного клиента"""
    permission_required = "customer.view_customer"

    queryset = Customer.objects.all().defer('created_at', 'updated_at')
    template_name = 'customer/customers-detail.html'


class CustomerCreate(PermissionRequiredMixin, CreateView):
    """Создание активного клиента"""
    permission_required = "customer.add_customer"

    queryset = (
        Customer.objects.all().defer('created_at', 'updated_at')
        .select_related('lead', 'lead__ad')
    )
    template_name = 'customer/customers-create.html'
    fields = 'lead', 'contract'

    success_url = reverse_lazy('customer:customer_list')

    def form_valid(self, form):
        # Обновление статистики рекламной компании при удалении активного клиента
        response = super().form_valid(form)
        lead = self.object.lead
        ad = lead.ad

        ad.customers_count += 1
        sum_contracts = Customer.objects.filter(lead__ad=ad).aggregate(
            total=Sum('contract__cost')
        )['total']

        if sum_contracts == 0:
            ad.profit = 0
        else:
            ad.profit = round((Decimal(str(sum_contracts)) / Decimal(str(ad.budget))), 2)

        ad.save()
        return response

class CustomerUpdate(PermissionRequiredMixin, UpdateView):
    """Обновление активного клиента"""
    permission_required = "customer.change_customer"

    queryset = Customer.objects.all().defer('created_at', 'updated_at')
    template_name = 'customer/customers-edit.html'
    fields = 'lead', 'contract'

    success_url = reverse_lazy('customer:customer_list')


class CustomerDelete(PermissionRequiredMixin, DeleteView):
    """Удаление потенциального клиента"""
    permission_required = "customer.delete_customer"

    queryset = (
        Customer.objects.all().defer('created_at', 'updated_at')
        .select_related('lead', 'lead__ad')
    )
    template_name = 'customer/customers-delete.html'

    success_url = reverse_lazy('customer:customer_list')

    def form_valid(self, form):
        # Обновление статистики рекламной компании при удалении активного клиента
        response = super().form_valid(form)
        lead = self.object.lead
        ad = lead.ad

        ad.customers_count -= 1
        sum_contracts = Customer.objects.filter(lead__ad=ad).aggregate(
            total=Sum('contract__cost')
        )['total']

        if sum_contracts == 0:
            ad.profit = 0
        else:
            ad.profit = round((Decimal(str(sum_contracts)) / Decimal(str(ad.budget))), 2)

        ad.save()
        return response
