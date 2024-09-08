from django.shortcuts import render, get_object_or_404
from .models import Mecanico


def listar_mecanicos(request):
    mecanicos = Mecanico.objects.all()
    return render(request, 'mecanicos/listar_mecanicos.html', {'mecanicos': mecanicos})


def detalhes_mecanico(request, mecanico_id):
    mecanico = get_object_or_404(Mecanico, pk=mecanico_id)
    return render(request, 'mecanicos/detalhes_mecanico.html', {'mecanico': mecanico})
