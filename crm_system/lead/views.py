from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Lead


class LeadListView(PermissionRequiredMixin, ListView):
    """Список потенциальных клиентов"""
    permission_required = 'lead.view_lead'

    model = Lead
    template_name = 'lead/lead-list.html'
    context_object_name = 'leads'


class LeadDetailView(PermissionRequiredMixin, DetailView):
    """Детали потенциального клиента"""
    permission_required = 'lead.view_lead'

    model = Lead
    template_name = 'lead/lead-detail.html'


class LeadCreateView(PermissionRequiredMixin, CreateView):
    """Создание потенциального клиента"""
    permission_required = 'lead.add_lead'

    model = Lead
    template_name = 'lead/lead-create.html'
    fields = '__all__'

    success_url = reverse_lazy('lead:lead_list')


class LeadUpdateView(PermissionRequiredMixin, UpdateView):
    """Обновление потенциального клиента"""
    permission_required = 'lead.change_lead'

    model = Lead
    template_name = 'lead/lead-update.html'
    fields = '__all__'

    success_url = reverse_lazy('lead:lead_list')


class LeadDeleteView(PermissionRequiredMixin, DeleteView):
    """Удаление потенциального клиента"""
    permission_required = 'lead.delete_lead'

    model = Lead
    template_name = 'lead/lead-delete.html'
    success_url = reverse_lazy('lead:lead_list')
