from django.shortcuts import render, get_object_or_404
from .models import ConsertoDeMoto


def listar_consertos(request):
    consertos = ConsertoDeMoto.objects.all()
    return render(request, 'consertos/listar_consertos.html', {'consertos': consertos})


def detalhes_conserto(request, conserto_id):
    conserto = get_object_or_404(ConsertoDeMoto, pk=conserto_id)
    return render(request, 'consertos/detalhes_conserto.html', {'conserto': conserto})
