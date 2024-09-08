import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mottu_manutencao.settings')
django.setup()

from consertos.models import ConsertoDeMoto, TipoConserto
from mecanicos.models import Mecanico

mecanicos_data = [
    {'id': 1, 'nome': 'Carlos', 'idade': 25, 'tempo_por_dia': 8, 'nivel_complexidade': 2},
    {'id': 2, 'nome': 'Ana', 'idade': 30, 'tempo_por_dia': 8, 'nivel_complexidade': 1},
    {'id': 3, 'nome': 'João', 'idade': 22, 'tempo_por_dia': 8, 'nivel_complexidade': 3},
    {'id': 4, 'nome': 'Mariana', 'idade': 28, 'tempo_por_dia': 8, 'nivel_complexidade': 2},
    {'id': 5, 'nome': 'Pedro', 'idade': 35, 'tempo_por_dia': 8, 'nivel_complexidade': 1},
    {'id': 6, 'nome': 'Julia', 'idade': 19, 'tempo_por_dia': 8, 'nivel_complexidade': 3},
    {'id': 7, 'nome': 'Ricardo', 'idade': 45, 'tempo_por_dia': 8, 'nivel_complexidade': 1},
    {'id': 8, 'nome': 'Fernanda', 'idade': 27, 'tempo_por_dia': 8, 'nivel_complexidade': 2},
    {'id': 9, 'nome': 'Thiago', 'idade': 32, 'tempo_por_dia': 8, 'nivel_complexidade': 3},
    {'id': 10, 'nome': 'Laura', 'idade': 24, 'tempo_por_dia': 8, 'nivel_complexidade': 1}
]

for mecanico in mecanicos_data:
    Mecanico.objects.get_or_create(
        id=mecanico['id'],
        defaults={
            'nome': mecanico['nome'],
            'idade': mecanico['idade'],
            'tempo_por_dia': mecanico['tempo_por_dia'],
            'nivel_complexidade': mecanico['nivel_complexidade']
        }
    )

tipos_conserto_data = [
    {'id': 1, 'tempo_estimado': 2},
    {'id': 2, 'tempo_estimado': 4},
    {'id': 3, 'tempo_estimado': 3},
    {'id': 4, 'tempo_estimado': 5},
    {'id': 5, 'tempo_estimado': 1},
]

for tipo_conserto in tipos_conserto_data:
    TipoConserto.objects.get_or_create(
        id=tipo_conserto['id'],
        defaults={'tempo_estimado': tipo_conserto['tempo_estimado']}
    )

consertos_data = [
    {'moto_id': 34, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 3, 'tempo_real': 4, 'data_entrada': '2024-07-10', 'mecanico_id': 2},
    {'moto_id': 294, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 1, 'tempo_real': 3, 'data_entrada': '2024-07-10', 'mecanico_id': 1},
    {'moto_id': 314, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 2, 'tempo_real': 2, 'data_entrada': '2024-07-10', 'mecanico_id': 7},
    {'moto_id': 488, 'complexidade_do_conserto': 3, 'tipo_conserto_id': 4, 'tempo_real': 1, 'data_entrada': '2024-07-10', 'mecanico_id': 6},
    {'moto_id': 123, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 3, 'tempo_real': 4, 'data_entrada': '2024-07-10', 'mecanico_id': 4},
    {'moto_id': 221, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 1, 'tempo_real': 2, 'data_entrada': '2024-07-10', 'mecanico_id': 10},
    {'moto_id': 456, 'complexidade_do_conserto': 3, 'tipo_conserto_id': 5, 'tempo_real': 5, 'data_entrada': '2024-07-11', 'mecanico_id': 9},
    {'moto_id': 89, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 2, 'tempo_real': 6, 'data_entrada': '2024-07-11', 'mecanico_id': 8},
    {'moto_id': 190, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 4, 'tempo_real': 1, 'data_entrada': '2024-07-11', 'mecanico_id': 7},
    {'moto_id': 402, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 3, 'tempo_real': 3, 'data_entrada': '2024-07-11', 'mecanico_id': 1},
    {'moto_id': 76, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 1, 'tempo_real': 4, 'data_entrada': '2024-07-11', 'mecanico_id': 10},
    {'moto_id': 320, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 5, 'tempo_real': 5, 'data_entrada': '2024-07-11', 'mecanico_id': 8},
    {'moto_id': 145, 'complexidade_do_conserto': 3, 'tipo_conserto_id': 2, 'tempo_real': 6, 'data_entrada': '2024-07-11', 'mecanico_id': 6},
    {'moto_id': 67, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 3, 'tempo_real': 1, 'data_entrada': '2024-07-11', 'mecanico_id': 2},
    {'moto_id': 290, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 4, 'tempo_real': 2, 'data_entrada': '2024-07-11', 'mecanico_id': 4},
    {'moto_id': 112, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 5, 'tempo_real': 4, 'data_entrada': '2024-07-11', 'mecanico_id': 7},
    {'moto_id': 404, 'complexidade_do_conserto': 3, 'tipo_conserto_id': 2, 'tempo_real': 1, 'data_entrada': '2024-07-12', 'mecanico_id': 9},
    {'moto_id': 310, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 3, 'tempo_real': 2, 'data_entrada': '2024-07-12', 'mecanico_id': 3},
    {'moto_id': 22, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 1, 'tempo_real': 4, 'data_entrada': '2024-07-12', 'mecanico_id': 8},
    {'moto_id': 459, 'complexidade_do_conserto': 3, 'tipo_conserto_id': 4, 'tempo_real': 1, 'data_entrada': '2024-07-12', 'mecanico_id': 6},
    {'moto_id': 134, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 5, 'tempo_real': 3, 'data_entrada': '2024-07-12', 'mecanico_id': 4},
    {'moto_id': 293, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 2, 'tempo_real': 2, 'data_entrada': '2024-07-12', 'mecanico_id': 10},
    {'moto_id': 378, 'complexidade_do_conserto': 3, 'tipo_conserto_id': 3, 'tempo_real': 4, 'data_entrada': '2024-07-12', 'mecanico_id': 6},
    {'moto_id': 101, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 4, 'tempo_real': 1, 'data_entrada': '2024-07-12', 'mecanico_id': 7},
    {'moto_id': 488, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 1, 'tempo_real': 3, 'data_entrada': '2024-07-12', 'mecanico_id': 8},
    {'moto_id': 376, 'complexidade_do_conserto': 3, 'tipo_conserto_id': 5, 'tempo_real': 5, 'data_entrada': '2024-07-12', 'mecanico_id': 9},
    {'moto_id': 184, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 2, 'tempo_real': 6, 'data_entrada': '2024-07-13', 'mecanico_id': 2},
    {'moto_id': 231, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 3, 'tempo_real': 4, 'data_entrada': '2024-07-13', 'mecanico_id': 1},
    {'moto_id': 498, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 4, 'tempo_real': 2, 'data_entrada': '2024-07-13', 'mecanico_id': 10},
    {'moto_id': 345, 'complexidade_do_conserto': 3, 'tipo_conserto_id': 1, 'tempo_real': 1, 'data_entrada': '2024-07-13', 'mecanico_id': 9},
    {'moto_id': 109, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 5, 'tempo_real': 3, 'data_entrada': '2024-07-13', 'mecanico_id': 4},
    {'moto_id': 203, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 3, 'tempo_real': 2, 'data_entrada': '2024-07-13', 'mecanico_id': 7},
    {'moto_id': 402, 'complexidade_do_conserto': 3, 'tipo_conserto_id': 2, 'tempo_real': 4, 'data_entrada': '2024-07-13', 'mecanico_id': 3},
    {'moto_id': 187, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 5, 'tempo_real': 1, 'data_entrada': '2024-07-13', 'mecanico_id': 2},
    {'moto_id': 291, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 4, 'tempo_real': 3, 'data_entrada': '2024-07-13', 'mecanico_id': 8},
    {'moto_id': 412, 'complexidade_do_conserto': 3, 'tipo_conserto_id': 1, 'tempo_real': 5, 'data_entrada': '2024-07-13', 'mecanico_id': 6},
    {'moto_id': 175, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 3, 'tempo_real': 6, 'data_entrada': '2024-07-14', 'mecanico_id': 4},
    {'moto_id': 64, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 2, 'tempo_real': 4, 'data_entrada': '2024-07-14', 'mecanico_id': 7},
    {'moto_id': 344, 'complexidade_do_conserto': 3, 'tipo_conserto_id': 4, 'tempo_real': 1, 'data_entrada': '2024-07-14', 'mecanico_id': 3},
    {'moto_id': 220, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 5, 'tempo_real': 3, 'data_entrada': '2024-07-14', 'mecanico_id': 1},
    {'moto_id': 128, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 3, 'tempo_real': 2, 'data_entrada': '2024-07-14', 'mecanico_id': 10},
    {'moto_id': 376, 'complexidade_do_conserto': 3, 'tipo_conserto_id': 2, 'tempo_real': 1, 'data_entrada': '2024-07-14', 'mecanico_id': 9},
    {'moto_id': 401, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 4, 'tempo_real': 4, 'data_entrada': '2024-07-14', 'mecanico_id': 2},
    {'moto_id': 147, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 1, 'tempo_real': 5, 'data_entrada': '2024-07-14', 'mecanico_id': 8},
    {'moto_id': 338, 'complexidade_do_conserto': 3, 'tipo_conserto_id': 3, 'tempo_real': 6, 'data_entrada': '2024-07-14', 'mecanico_id': 6},
    {'moto_id': 178, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 2, 'tempo_real': 1, 'data_entrada': '2024-07-14', 'mecanico_id': 7},
    {'moto_id': 234, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 5, 'tempo_real': 3, 'data_entrada': '2024-07-14', 'mecanico_id': 4},
    {'moto_id': 97, 'complexidade_do_conserto': 3, 'tipo_conserto_id': 4, 'tempo_real': 2, 'data_entrada': '2024-07-14', 'mecanico_id': 9},
    {'moto_id': 120, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 3, 'tempo_real': 4, 'data_entrada': '2024-07-14', 'mecanico_id': 3},
    {'moto_id': 221, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 1, 'tempo_real': None, 'data_entrada': '2024-07-15', 'mecanico_id': None},
    {'moto_id': 154, 'complexidade_do_conserto': 3, 'tipo_conserto_id': 5, 'tempo_real': None, 'data_entrada': '2024-07-15', 'mecanico_id': None},
    {'moto_id': 299, 'complexidade_do_conserto': 1, 'tipo_conserto_id': 2, 'tempo_real': None, 'data_entrada': '2024-07-15', 'mecanico_id': None},
    {'moto_id': 432, 'complexidade_do_conserto': 2, 'tipo_conserto_id': 4, 'tempo_real': None, 'data_entrada': '2024-07-15', 'mecanico_id': None},
    {'moto_id': 75, 'complexidade_do_conserto': 3, 'tipo_conserto_id': 3, 'tempo_real': None, 'data_entrada': '2024-07-15', 'mecanico_id': None},
]

for conserto in consertos_data:
    ConsertoDeMoto.objects.get_or_create(
        moto_id=conserto['moto_id'],
        complexidade_do_conserto=conserto['complexidade_do_conserto'],
        tipo_conserto_id=conserto['tipo_conserto_id'],
        tempo_real=conserto['tempo_real'],
        data_entrada=conserto['data_entrada'],
        mecanico_id=conserto['mecanico_id']
    )

print("Dados inseridos com sucesso!")
