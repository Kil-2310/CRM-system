from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Lead


class LeadListView(PermissionRequiredMixin, ListView):
    """Список потенциальных клиентов"""
    permission_required = 'lead.view_lead'

    queryset = Lead.objects.all().defer('created_at', 'updated_at')
    template_name = 'lead/leads-list.html'
    context_object_name = 'leads'


class LeadDetailView(PermissionRequiredMixin, DetailView):
    """Детали потенциального клиента"""
    permission_required = 'lead.view_lead'

    queryset = Lead.objects.all().defer('created_at', 'updated_at')
    template_name = 'lead/leads-detail.html'


class LeadCreateView(PermissionRequiredMixin, CreateView):
    """Создание потенциального клиента"""
    permission_required = 'lead.add_lead'

    queryset = Lead.objects.all().defer('created_at', 'updated_at')
    template_name = 'lead/leads-create.html'
    fields = 'first_name', 'last_name', 'email', 'phone'

    success_url = reverse_lazy('lead:lead_list')


class LeadUpdateView(PermissionRequiredMixin, UpdateView):
    """Обновление потенциального клиента"""
    permission_required = 'lead.change_lead'

    queryset = Lead.objects.all().defer('created_at', 'updated_at')
    template_name = 'lead/leads-edit.html'
    fields = 'first_name', 'last_name', 'email', 'phone'

    success_url = reverse_lazy('lead:lead_list')


class LeadDeleteView(PermissionRequiredMixin, DeleteView):
    """Удаление потенциального клиента"""
    permission_required = 'lead.delete_lead'

    queryset = Lead.objects.all().defer('created_at', 'updated_at')
    template_name = 'lead/leads-delete.html'

    success_url = reverse_lazy('lead:lead_list')
