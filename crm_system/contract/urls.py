from django.urls import path

from .views import (
    ContractListView,
    ContractCreateView,
    ContractDeleteView,
    ContractDetailView,
    ContractUpdateView,
)


app_name = 'contract'

urlpatterns = [
    path('', ContractListView.as_view(), name='contract_list'),
    path('new/', ContractCreateView.as_view(), name='contract_create'),
    path('<int:pk>/', ContractDetailView.as_view(), name='contract_detail'),
    path('<int:pk>/edit/', ContractUpdateView.as_view(), name='contract_update'),
    path('<int:pk>/delete/', ContractDeleteView.as_view(), name='contract_delete'),
]
