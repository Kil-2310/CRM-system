from django.urls import path

from .views import ApplicationMetricsListView


app_name = 'user'

urlpatterns = [
    path('', ApplicationMetricsListView.as_view(), name='application_metrics_list'),
]
