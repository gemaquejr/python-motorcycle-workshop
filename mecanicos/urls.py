from django.urls import path
from .views import listar_mecanicos, detalhes_mecanico

urlpatterns = [
    path('', listar_mecanicos, name='listar_mecanicos'),
    path('<int:mecanico_id>/', detalhes_mecanico, name='detalhes_mecanico'),
]
