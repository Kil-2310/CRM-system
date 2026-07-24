from django.urls import path

from .views import (
    CustomerList,
    CustomerDetail,
    CustomerCreate,
    CustomerUpdate,
    CustomerDelete,
)


app_name = 'customer'

urlpatterns = [
    path('', CustomerList.as_view(), name='customer_list'),
    path('<int:pk>/', CustomerDetail.as_view(), name='customer_detail'),
    path('create/', CustomerCreate.as_view(), name='customer_create'),
    path('<int:pk>/edit/', CustomerUpdate.as_view(), name='customer_update'),
    path('<int:pk>/delete/', CustomerDelete.as_view(), name='customer_delete'),
]
