from django.urls import path

from .views import (
    LeadListView,
    LeadCreateView,
    LeadDeleteView,
    LeadDetailView,
    LeadUpdateView,
)


app_name = 'lead'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead_list'),
    path('new/', LeadCreateView.as_view(), name='lead-create'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/edit/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
]
