from django.db import models

# Create your models here.


class Estacion(models.Model):

    uid = models.IntegerField()
    ultima_actualizacion = models.DateTimeField()
    direccion = models.CharField(max_length=80)
    codigo_postal = models.CharField(max_length=80)
    slots = models.IntegerField()
    cant_bicicletas_n = models.IntegerField()  # bicicletas normales
    bicicletas_e = models.BooleanField()
    cant_bicicletas_e = models.IntegerField()  # bicicletas elétricas
    arrendando = models.IntegerField()
    devolviendo = models.IntegerField()
    terminal_pago = models.BooleanField(max_length=80)
    formas_pago = models.CharField(max_length=80)

    def __str__(self):
        return f'UID: {self.uid} - Dirección: {self.direccion}'
