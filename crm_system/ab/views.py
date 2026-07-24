from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Ab


class AbListView(PermissionRequiredMixin, ListView):
    """Список рекламных компаний"""
    permission_required = 'ab.view_ab'

    queryset = Ab.objects.all().defer('created_at', 'updated_at')
    template_name = "abs/abs-list.html"
    context_object_name = 'abs'


class AbDetailView(DetailView):
    """Детали рекламной компании"""
    permission_required = 'ab.view_ab'

    queryset = Ab.objects.all().defer('created_at', 'updated_at')
    template_name = "abs/abs-detail.html"


class AbCreateView(PermissionRequiredMixin, CreateView):
    """Создание рекламной компании"""
    permission_required = 'ab.add_ab'

    queryset = Ab.objects.all().defer('created_at', 'updated_at')
    template_name = "abs/abs-create.html"

    success_url = reverse_lazy('ab:ab-list')


class AbUpdateView(PermissionRequiredMixin, UpdateView):
    """Обновление рекламной компании"""
    permission_required = 'ab.change_ab'

    queryset = Ab.objects.all().defer('created_at', 'updated_at')
    template_name = "abs/abs-update.html"

    success_url = reverse_lazy('ab:ab-list')


class AbDeleteView(PermissionRequiredMixin, DeleteView):
    """Удаление рекламной компании"""
    permission_required = 'ab.delete_ab'

    queryset = Ab.objects.all().defer('created_at', 'updated_at')
    template_name = "abs/abs-delete.html"

    success_url = reverse_lazy('ab:ab-list')


class AdStatisticView(PermissionRequiredMixin, ListView):
    """Получение статистики рекламных компаний"""
    permission_required = 'ab.view_ab'

    queryset = Ab.objects.all().defer('created_at', 'updated_at')
    template_name = "abs/abs-statistic.html"
