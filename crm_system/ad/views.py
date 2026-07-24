from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Ad


class AdListView(PermissionRequiredMixin, ListView):
    """Список рекламных компаний"""
    permission_required = 'ad.view_ad'

    queryset = Ad.objects.all().defer('created_at', 'updated_at')
    template_name = "ad/ads-list.html"
    context_object_name = 'ads'


class AdDetailView(DetailView):
    """Детали рекламной компании"""
    permission_required = 'ad.view_ad'

    queryset = Ad.objects.all().defer('created_at', 'updated_at')
    template_name = "ad/ads-detail.html"


class AdCreateView(PermissionRequiredMixin, CreateView):
    """Создание рекламной компании"""
    permission_required = 'ad.add_ad'

    queryset = Ad.objects.all().defer('created_at', 'updated_at')
    template_name = "ad/ads-create.html"
    fields = 'name', 'budget', 'channel', 'product'

    success_url = reverse_lazy('ad:ad-list')


class AdUpdateView(PermissionRequiredMixin, UpdateView):
    """Обновление рекламной компании"""
    permission_required = 'ad.change_ad'

    queryset = Ad.objects.all().defer('created_at', 'updated_at')
    template_name = "ad/ads-update.html"
    fields = 'name', 'budget', 'channel', 'product'

    success_url = reverse_lazy('ad:ad-list')


class AdDeleteView(PermissionRequiredMixin, DeleteView):
    """Удаление рекламной компании"""
    permission_required = 'ad.delete_ad'

    queryset = Ad.objects.all().defer('created_at', 'updated_at')
    template_name = "ad/ads-delete.html"

    success_url = reverse_lazy('ad:ad-list')


class AdStatisticView(PermissionRequiredMixin, ListView):
    """Получение статистики рекламных компаний"""
    permission_required = 'ad.view_ad'

    queryset = Ad.objects.all().defer('created_at', 'updated_at')
    template_name = "ad/ads-statistic.html"
