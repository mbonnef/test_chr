from django.db import models

# Create your models here.


class Proyecto(models.Model):

    no = models.IntegerField()
    nombre = models.CharField(max_length=80)
    tipo = models.CharField(max_length=80)
    region = models.CharField(max_length=80)
    tipologia = models.CharField(max_length=80)
    titular = models.CharField(max_length=80)
    inversion = models.FloatField()
    fecha = models.DateField()
    estado = models.CharField(max_length=80)

    def __str__(self):
        return f'N°: {self.no} - Nombre: {self.nombre}'
