from django.shortcuts import render, HttpResponse
from .models import *
from TCI.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def prueba(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def exit(request):
    logout(request)
    return render(request,'home.html')

def lista_equipos(request):
    equipos = Equipo.objects.all()
    data = []

    for equipo in equipos:
        participantes = Participante.objects.filter(equipo=equipo)
        data.append({'equipo': equipo, 'participantes': participantes})
        return render(request, 'pruebaequipos.html', {'data': data})
    
@login_required
def temporadas(request):
    temporadas = Temporada.objects.all()
    return render(request, "temporadas.html", {'temporadas': temporadas})

@login_required
def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, "equipos.html", {'equipos': equipos})

@login_required
def participantes(request):
    participantes = Participante.objects.all()
    return render(request, "participantes.html", {'participantes': participantes})

@login_required
def temporada(request):
    return render(request, "detallesTemporada.html")

@login_required
def equipo(request):
    return render(request, "detallesEquipo.html")

@login_required
def participante(request):
    return render(request, "detallesParticipante.html")