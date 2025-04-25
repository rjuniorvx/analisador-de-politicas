from django.urls import path

from .api_views import (
    PoliticaCreateView,
    PoliticaListView,
    PoliticaDetailView,
    PoliticaAnaliseAPIView
)

urlpatterns = [
    path('politicas/', PoliticaListView.as_view(), name='api-politica-list'),
    path('politicas/criar/', PoliticaCreateView.as_view(), name='api-politica-create'),
    path('politicas/<int:pk>/', PoliticaDetailView.as_view(), name='api-politica-detail'),
    path('politicas/<int:pk>/analise/', PoliticaAnaliseAPIView.as_view(), name='api-analise'),
]