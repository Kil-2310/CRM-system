from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Product


class ProductListView(PermissionRequiredMixin, ListView):
    """Список продуктов"""
    permission_required = "product.view_product"

    queryset = Product.objects.all().defer('created_at', 'updated_at')
    template_name = "product/products-list.html"
    context_object_name = "products"


class ProductDetailView(PermissionRequiredMixin, DetailView):
    """Детали продукта"""
    permission_required = "product.view_product"

    queryset = Product.objects.all().defer('created_at', 'updated_at')
    template_name = "product/products-detail.html"


class ProductCreateView(PermissionRequiredMixin, CreateView):
    """Создание продукта"""
    permission_required = "product.add_product"

    queryset = Product.objects.all().defer('created_at', 'updated_at')
    template_name = "product/products-create.html"
    fields = "name", "description", "cost"

    success_url = reverse_lazy("product:product_list")


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    """Обновление продукта"""
    permission_required = "product.change_product"

    queryset = Product.objects.all().defer('created_at', 'updated_at')
    template_name = "product/products-edit.html"
    fields = "name", "description", "cost"

    success_url = reverse_lazy("product:product_list")


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    """Удаление продукта"""
    permission_required = "product.delete_product"

    queryset = Product.objects.all().defer('created_at', 'updated_at')
    template_name = "product/products-delete.html"

    success_url = reverse_lazy("product:product_list")
