from django.db import models

class Habilidad(models.Model):
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
    descripcion = models.CharField(max_length=100)

class Participante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    apodo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    estadoParticipacion = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    habilidad = models.ForeignKey(Habilidad, on_delete=models.CASCADE)


    def agregarParticipante(self, nombre, descripcion, apellido, pais, habilidad, apodo, estadoParticipacion):
        nuevo_participante = Participante(
            nombre=nombre,
            descripcion=descripcion,
            apellido=apellido,
            pais=pais,
            habilidad=habilidad,
            apodo=apodo,
            estadoParticipacion=estadoParticipacion
        )
        nuevo_participante.save()
        return nuevo_participante

    def eliminarParticipante(self):
        self.delete()

    def cambiarEstado(self, nuevo_estado):
        self.estadoParticipacion = nuevo_estado
        self.save()

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    puntos = models.IntegerField(default=0)
    participantes = models.ForeignKey(Participante, on_delete=models.CASCADE)

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

class Alianza(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField()
    listaEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def formaralianza(self, nueva_alianza):
        self.nombre = nueva_alianza

class Reglas(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

class Desafio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    equipos = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    reglas = models.ForeignKey(Reglas, on_delete=models.CASCADE)

class Detalle_desafio(models.Model):
    puntos = models.IntegerField()
    fechadesafio = models.DateField()
    ganador = models.ForeignKey(Equipo, on_delete=models.CASCADE)

class RondaEliminacion(models.Model):
    fechaRondaEliminacion = models.DateField()
    eliminado = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __init__(self):
        self.eliminado = None

    def eliminarEquipo(self, equipo):
        self.eliminado = equipo

class Temporada(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()
    ganador = models.CharField(max_length=40, blank=True, null=True)
    listaEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, null=True, blank=True)
    listaAlianza = models.ForeignKey(Alianza, on_delete=models.CASCADE, null=True, blank=True)
    listaDesafio = models.ForeignKey(Desafio, on_delete=models.CASCADE, null=True, blank=True)
    listaDetalleDesafio = models.ForeignKey(Detalle_desafio, on_delete=models.CASCADE, null=True, blank=True)
    listaRondaEliminacion = models.ForeignKey(RondaEliminacion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'"{self.nombre}" temporada numero {self.numero}' 
    
    def conocerEquipos(self):
        return self.listaEquipo.all()
    
    def conocerAlianzas(self):
        return self.listaAlianza.all()
    
    def conocerDesafios(self):
        return self.listaDesafio.all()
    
    def conocerDetallesDesafios(self):
        return self.listaDetalleDesafio.all()
    
    def conocerRondasEliminacion(self):
        return self.listaRondaEliminacion.all()
    
    def listaEquipos(self):
        equipos = self.listaEquipo.all()
        return [equipo.nombre for equipo in equipos]
    
    def listaAlianzas(self):
        alianzas = self.listaAlianza.all()
        return [alianza.nombre for alianza in alianzas]
    
    def listaDesafios(self):
        desafios = self.listaDesafio.all()
        return [desafio.nombre for desafio in desafios]
    
    def listaRondasELiminacion(self):
        rondas = self.listaRondaEliminacion.all()
        return [ronda.nombre for ronda in rondas]
    
    def listaDetalleDesafio(self):
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



