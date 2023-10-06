from django.shortcuts import render, HttpResponse
from TCI.models import *

# Create your views here.

def home(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def prueba(request):
    paises = Participante.objects.all()
    
    return render(request, "prueba.html", {'paises': paises})

def temporadas(request):
    temporadas = Temporada.objects.all()
    return render(request, "temporadas.html", {'temporadas': temporadas})