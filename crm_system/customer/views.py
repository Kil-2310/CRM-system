from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

    queryset = Customer.objects.all().defer('created_at', 'updated_at')
    template_name = 'customer/customers-create.html'
    fields = ('lead' ,)

    success_url = reverse_lazy('customer:customer_list')


class CustomerUpdate(PermissionRequiredMixin, UpdateView):
    """Обновление активного клиента"""
    permission_required = "customer.change_customer"

    queryset = Customer.objects.all().defer('created_at', 'updated_at')
    template_name = 'customer/customers-edit.html'
    fields = ('lead' ,)

    success_url = reverse_lazy('customer:customer_list')


class CustomerDelete(PermissionRequiredMixin, DeleteView):
    """Удаление потенциального клиента"""
    permission_required = "customer.delete_customer"

    queryset = Customer.objects.all().defer('created_at', 'updated_at')
    template_name = 'customer/customers-delete.html'

    success_url = reverse_lazy('customer:customer_list')
