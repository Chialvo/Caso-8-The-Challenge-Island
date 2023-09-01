from django.db import models

from django.db import models

class Temporada(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()

    def __str__(self):
        return f'"{self.nombre}" temporada numero {self.numero}'