from django.db import models


class Mecanico(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    tempo_por_dia = models.IntegerField(default=8)
    nivel_complexidade = models.IntegerField()

    def __str__(self):
        return self.nome
