from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, reverse
from django.urls import reverse_lazy

from .models import Product


# Роль - Маркетолог

class ProductListView(ListView):
    """Список продуктов"""
    model = Product
    template_name = "product/products-list.html"


class ProductDetailView(DetailView):
    """Детали продукта"""
    model = Product
    template_name = "product/products-detail.html"


class ProductCreateView(CreateView):
    """Создание продукта"""
    model = Product
    template_name = "product/products-create.html"
    fields = "__all__"


class ProductUpdateView(UpdateView):
    """Обновление продукта"""
    model = Product
    template_name = "product/products-update.html"
    fields = "__all__"


class ProductDeleteView(DeleteView):
    """Удаление продукта"""
    model = Product
    template_name = "product/products-delete.html"
