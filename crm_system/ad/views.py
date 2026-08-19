from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Ad
from .tasks import update_ad_profit


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
        update_ad_profit.delay(self.object)
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
