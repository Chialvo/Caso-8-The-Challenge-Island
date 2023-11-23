from django.db.models import Q
from .models import *


def buscarTemporada( busqueda):
    temporadas = Temporada.objects.all()
    try:
        temporada_relacionada = temporadas.filter(
            Q(nombre__icontains=busqueda) |
            Q(numero=busqueda) |
            Q(puntos=busqueda)).distinct()
    except ValueError:
        temporada_relacionada = temporadas.filter(
            Q(nombre__icontains=busqueda)).distinct()
    temporada_no_relacionadas = temporadas.exclude(id__in=temporada_relacionada.values_list('id', flat=True))
    resultado = list(temporada_relacionada) + list(temporada_no_relacionadas)
    return resultado

def buscarEquipo(busqueda):
    equipos = Equipo.objects.all()
    equipo_relacionado = equipos.filter(
        Q(nombre__icontains=busqueda) | Q()).distinc()
    equipo_no_relacionado = equipos.exclude(id__in=equipo_relacionado.values_list('id', flat=True))
    resultado = list(equipo_relacionado) + list(equipo_no_relacionado)
    return resultado

def buscarParticipante(busqueda):
    participantes = Participante.objects.all()
    participante_relacionado = participantes.filter(
        Q(nombre__icontains=busqueda) |
        Q(apellido__icontains=busqueda) |
        Q(apodo__icontains=busqueda) |
        Q(pais__nombre__icontains=busqueda) |
        Q()).distinct()
    participantes_no_relacionado = participantes.exclude(id__in=participante_relacionado.values_list('id', flat=True))
    resultado = list(participante_relacionado) + list(participantes_no_relacionado)
    return resultado

def buscar_generico(queryset, busqueda,):
    campos = [campo.name for campo in queryset.model._meta.get_fields()]
    resultados_relacionados = queryset.filter(
        Q(**{f'{campo}__icontains': busqueda}) for campo in campos).distinct()
    resultados_no_relacionados = queryset.exclude(
        id__in=resultados_relacionados.values_list('id', flat=True)
    )
    resultado_final = list(resultados_relacionados) + list(resultados_no_relacionados)
    return resultado_final