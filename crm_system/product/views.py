from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Product
from utils.group_mixin import GroupRequiredMixin


class ProductListView(ListView):
    """Список продуктов"""
    model = Product
    template_name = "product/products-list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    """Детали продукта"""
    model = Product
    template_name = "product/products-detail.html"


class ProductCreateView(GroupRequiredMixin, CreateView):
    """Создание продукта"""
    group_required = 'Managers'

    model = Product
    template_name = "product/products-create.html"
    fields = "name", "description", "cost"

    success_url = reverse_lazy("product:product_list")


class ProductUpdateView(GroupRequiredMixin, UpdateView):
    """Обновление продукта"""
    group_required = 'Managers'

    model = Product
    template_name = "product/products-edit.html"
    fields = "name", "description", "cost"

    success_url = reverse_lazy("product:product_list")


class ProductDeleteView(GroupRequiredMixin, DeleteView):
    """Удаление продукта"""
    group_required = 'Managers'

    model = Product
    template_name = "product/products-delete.html"

    success_url = reverse_lazy("product:product_list")
