from django.urls import path

from .views import (
    AdListView,
    AdDetailView,
    AdCreateView,
    AdUpdateView,
    AdDeleteView,
    AdStatisticView
)


app_name = 'ad'

urlpatterns = [
    path('', AdListView.as_view(), name='ab_list'),
    path('<int:pk>/', AdDetailView.as_view(), name='ab_detail'),
    path('new/', AdCreateView.as_view(), name='ab_create'),
    path('<int:pk>/edit/', AdUpdateView.as_view(), name='ab_update'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name='ab_delete'),
    path('statistic/', AdStatisticView.as_view(), name='ad_statistic'),
]
