from django.db import models
from mecanicos.models import Mecanico


class TipoConserto(models.Model):
    tempo_estimado = models.IntegerField()


class ConsertoDeMoto(models.Model):
    moto_id = models.IntegerField(default=0)
    complexidade_do_conserto = models.IntegerField()
    tipo_conserto = models.ForeignKey(TipoConserto, on_delete=models.CASCADE)
    tempo_real = models.IntegerField(null=True, blank=True)
    data_entrada = models.DateField()
    mecanico = models.ForeignKey(Mecanico, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Moto {self.id} - Conserto {self.tipo_conserto}"
