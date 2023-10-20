from django.shortcuts import render, HttpResponse
<<<<<<< HEAD
from .models import *
=======
from TCI.models import *
>>>>>>> dad438aaa939acd703e7b89d790b5e03da74fe30

# Create your views here.

def home(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

<<<<<<< HEAD
def lista_equipos(request):
    equipos = Equipo.objects.all()
    data = []

    for equipo in equipos:
        participantes = Participante.objects.filter(equipo=equipo)
        data.append({'equipo': equipo, 'participantes': participantes})
        return render(request, 'pruebaequipos.html', {'data': data})
=======
def prueba(request):
    paises = Participante.objects.all()
    
    return render(request, "prueba.html", {'paises': paises})

def temporadas(request):
    temporadas = Temporada.objects.all()
    return render(request, "temporadas.html", {'temporadas': temporadas})

def equipo(request):
    equipos = Equipo.objects.all()
    return render(request, "equipos.html", {'equipos': equipos})
>>>>>>> dad438aaa939acd703e7b89d790b5e03da74fe30
