from django.urls import path
from .views import listar_consertos, detalhes_conserto

urlpatterns = [
    path('', listar_consertos, name='listar_consertos'),
    path('<int:conserto_id>/', detalhes_conserto, name='detalhes_conserto'),
]
