from django.urls import path

from .views import (
    ProductDetailView,
    ProductListView,
    ProductDeleteView,
    ProductCreateView,
    ProductUpdateView
)


app_name = "product"

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('new/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
