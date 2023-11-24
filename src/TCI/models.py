from django.db import models
from django.core.validators import FileExtensionValidator

class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def setDescripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def getDescripcion(self):
        return self.descripcion

    def crear(cls, descripcion):
        nueva_habilidad = cls(descripcion=descripcion)
        nueva_habilidad.save()
        return nueva_habilidad

    def __str__(self):
        return self.descripcion

class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.nombre}"

class Participante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    apodo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    estadoParticipacion = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    habilidad = models.ForeignKey(Habilidad, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='static/img/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], default='static/img/defaultprofile.jpg')

    def __str__(self) -> str:
        return f"{self.nombre}"

    def eliminarParticipante(self):
        self.delete()

    def cambiarEstado(self, nuevo_estado):
        self.estadoParticipacion = nuevo_estado
        self.save()

class Alianza(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)
    Equipos = models.ManyToManyField('Equipo')

    def __str__(self) -> str:
        return f"{self.nombre}"

    def formaralianza(self, nueva_alianza):
        self.nombre = nueva_alianza


class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    participantes = models.ManyToManyField('Participante')
    alianzas = models.ManyToManyField('Alianza')
    foto = models.ImageField(upload_to='static/img/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], default='static/img/defaultprofile')

    def conoceraparticipantes(self, participante):
        self.participantes.add(participante)

    def listarparticipantes(self):
        Participantes = self.participantes.all()
        return Participantes 
    
    def formarAlianza(self, nueva_alianza):
        self.nombre = nueva_alianza
        self.save()

    def estadoAlianza(self):
        pass

    def __str__(self):
        return self.nombre

class Regla(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

class Desafio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    equipos = models.ManyToManyField('Equipo')
    reglas = models.ManyToManyField("Regla")

class Detalle_desafio(models.Model):
    puntos = models.IntegerField(unique=True, default=0)
    fechadesafio = models.DateField()
    ganador = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    desafios = models.ForeignKey(Desafio, null=True, on_delete=models.CASCADE)

class RondaEliminacion(models.Model):
    fechaRondaEliminacion = models.DateField()
    eliminado = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    desafio = models.ForeignKey(Desafio, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Ronda de eliminación ({self.fechaRondaEliminacion})'

    def eliminarEquipo(self, equipo):
        self.eliminado = equipo

class Temporada(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()
    listaEquipo = models.ManyToManyField("Equipo")
    listaAlianza = models.ForeignKey(Alianza, on_delete=models.CASCADE, null=True, blank=True)
    listaDetalleDesafio = models.ManyToManyField("Detalle_desafio", related_name="temporada_detalle_desafio")
    listaRondaEliminacion = models.ForeignKey(RondaEliminacion, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='static/img/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], default='static/img/defaultprofile')
    
    

    def __str__(self):
        return f'"{self.nombre}" temporada numero {self.numero}' 
    
    def listaEquipos(self):
        pass
    
    def listaAlianzas(self):
        pass
    
    def listaRondasELiminacion(self):
        pass
    
    def listaDetalleDesafios(self):
        detalles = self.listaDetalleDesafio.all()
        return [detalle.nombre for detalle in detalles]
    
    def enviarEquipos(self):
        pass
    
    def calcularPuntos(self):
        pass
    
    def generarTabla(self):
        pass
    
    def actualizarTabla(self):
        pass

    def calcularGanador(self):
        equipos = self.listaEquipo.all()
        ganador = None
        max_puntos = 0

        for equipo in equipos:
            if equipo.puntos and equipo.puntos.puntos > max_puntos:
                max_puntos = equipo.puntos.puntos
                ganador = equipo

        return ganador



