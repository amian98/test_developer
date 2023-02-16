from django.db import models

# Create your models here.

class SEIA(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=500)
    tipo = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    tipologia = models.CharField(max_length=200)
    titular = models.CharField(max_length=200)
    inversion = models.FloatField()
    fecha = models.DateField()
    estado = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

