from django.shortcuts import render, HttpResponse
from .models import *
from TCI.models import *


# Create your views here.

def home(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def lista_equipos(request):
    equipos = Equipo.objects.all()
    data = []

    for equipo in equipos:
        participantes = Participante.objects.filter(equipo=equipo)
        data.append({'equipo': equipo, 'participantes': participantes})
        return render(request, 'pruebaequipos.html', {'data': data})

def prueba(request):
    paises = Participante.objects.all()
    
    return render(request, "prueba.html", {'paises': paises})

def temporadas(request):
    temporadas = Temporada.objects.all()
    return render(request, "temporadas.html", {'temporadas': temporadas})

def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, "equipos.html", {'equipos': equipos})