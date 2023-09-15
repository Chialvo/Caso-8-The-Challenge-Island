from django.db import models


class Equipo(models.Model):
    nombre = models.CharField(max_length=100)

    def conoceraparticipantes(self, participante):
        self.participantes.add(participante)

    def listarparticipantes(self):
        Participantes = self.participantes.all()
        return Participantes 


class Participantes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    apodo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    habilidad = models.CharField(max_length=50)
    estado_participacion = models.CharField(max_length=50)

class Temporada(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()
    ganador = models.CharField(max_length=40)

    def __str__(self):
        return f'"{self.nombre}" temporada numero {self.numero}' 


class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

class Desafio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    reglas = models.CharField(max_length=50)

class Detalle_desafio(models.Model):
    puntos = models.IntegerField()
    fechadesafio = models.DateField()

class RondaEliminacion(models.Model):
    eliminado = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __init__(self):
        self.eliminado = None

    def eliminarEquipo(self, equipo):
        self.eliminado = equipo


class Reglas(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

class Alianza(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def formaralianza(self, nueva_alianza):
        self.nombre = nueva_alianza


