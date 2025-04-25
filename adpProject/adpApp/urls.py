from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_politicas, name='listar_politicas'),
    path('criar/', views.criar_politica, name='criar_politica'),
    path('politica/<int:politica_id>/', views.ver_politica, name='ver_politica'),
    path('politica/<int:politica_id>/analisar/', views.analisar_politica, name='analisar_politica'),
]