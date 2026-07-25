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
    path('', AdListView.as_view(), name='ad_list'),
    path('<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('new/', AdCreateView.as_view(), name='ad_create'),
    path('<int:pk>/edit/', AdUpdateView.as_view(), name='ad_update'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name='ad_delete'),
    path('statistic/', AdStatisticView.as_view(), name='ad_statistic'),
]
