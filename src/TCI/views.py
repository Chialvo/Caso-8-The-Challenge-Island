from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from TCI.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q


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
    equipo_no_relacionado = participantes.exclude(id__in=equipo_relacionado.values_list('id', flat=True))
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

def home(request):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarTemporada(request, busqueda)
        return render(request, 'temporadas.html', {'temporadas': resultado})
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def exit_tci(request):
    logout(request)
    return redirect('home')


@login_required
def temporadas(request):
    temporadas = Temporada.objects.all()
    return render(request, "temporadas.html", {'temporadas': temporadas})
@login_required
def temporada(request):
    return render(request, "detallesTemporada.html")
@login_required
def temporadaForm(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        numero = request.POST.get('numero')
        
        # Crea una nueva temporada
        temporada = Temporada(nombre=nombre, numero=numero)
        temporada.save()
        
        return redirect('detalle_temporada', pk=temporada.pk)  # Asegúrate de definir 'detalle_temporada' en tus URLs

    return render(request, 'forms/temporadaForm.html')





@login_required
def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, "equipos.html", {'equipos': equipos})
@login_required
def equipo(request, pk):
    equipo = Equipo.objects.get(pk=pk)
    nombre = equipo.nombre
    listaParticipantes = equipo.listarparticipantes()
    print('---'*10      )
    print(listaParticipantes)
    return render(request, "detallesEquipo.html", {'nombre': nombre, 'listaParticipantes': listaParticipantes})
@login_required
def equipoForm(request):
    if request.method == 'POST':
        nombre_equipo = request.POST.get('nombre_equipo')
        seleccionados=None
        seleccionados = request.POST.getlist('seleccionados')
        print('-'*20)
        participantes = Participante.objects.all()
        for i in seleccionados:
            for x in participantes:
                if int(i)==x.pk:
                    print(x.nombre)
        print('-'*20)
        equipo = Equipo(nombre=nombre_equipo)
        equipo.save()

        for participante_id in seleccionados:
            participante = Participante.objects.get(pk=participante_id)
            equipo.participantes.add(participante)

        return redirect('equipo', pk=equipo.pk)

    participantes = Participante.objects.all()
    return render(request, 'forms/equipoForm.html', {"participantes": participantes})




@login_required
def participantes(request):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarParticipante(busqueda)
        return render(request, 'participantes.html', {'participantes': resultado})
    participantes = Participante.objects.all()
    return render(request, "participantes.html", {'participantes': participantes})
@login_required
def participante(request, pk):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarParticipante(busqueda)
        return render(request, 'participantes.html', {'participantes': resultado})
    participante = Participante.objects.get(pk=pk)
    nombre = participante.nombre
    apellido = participante.apellido
    apodo = participante.apodo
    descripcion = participante.descripcion
    estado = participante.estadoParticipacion
    pais = participante.pais
    habilidad = participante.habilidad

    return render(request, "detallesParticipante.html", {
        'participante': participante,
        'nombre': nombre,
        'apellido': apellido,
        'apodo': apodo,
        'descripcion': descripcion,
        'estado': estado,
        'pais': pais,
        'habilidad': habilidad
    })
@login_required
def participanteForm(request):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarParticipante(busqueda)
        return render(request, 'participantes.html', {'participantes': resultado})
    if request.method == 'POST':
        # Procesa los datos del formulario POST
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        apodo = request.POST.get('apodo')
        descripcion = request.POST.get('descripcion')
        estado_participacion = request.POST.get('estado_participacion')
        habilidad_id = request.POST.get('habilidad')
        pais_id = request.POST.get('pais')
        paises = Pais.objects.all()
        habilidades = Habilidad.objects.all()

        for i in habilidades:
            if i.descripcion == habilidad_id:
                habilidad = i
                break
        else:
            return HttpResponse('Habilidad no encontrada. Por favor, verifica tu selección.')

        for p in paises:
            if p.nombre == pais_id:
                pais = p
                break
        else:
            return HttpResponse('País no encontrado. Por favor, verifica tu selección.')
        

        participante = Participante(
            nombre=nombre,
            apellido=apellido,
            apodo=apodo,
            descripcion=descripcion,
            estadoParticipacion=estado_participacion,
            habilidad=habilidad,
            pais=pais
        )
        participante.save()
        
        return redirect('participante', pk=participante.pk)
    
    paises = Pais.objects.all()
    habilidades = Habilidad.objects.all()
    return render(request, 'forms/participanteForm.html', {'paises': paises, 'habilidades': habilidades})



def homeAdmin(request):
    return render(request, "admin/homeAdmin.html")


def accionAdmin(request, num):
    nombre_dict = {
        1: 'Temporada',
        2: 'Equipo',
        3: 'Participante',
        4: 'Pais',
        5: 'Alianza',
        6: 'Habilidad',
        7: 'Regla',
        8: 'Desafio',
        9: 'Ronda Eliminacion',
    }
    forms_dict = {
        1: 'temporadaForm',
        2: 'equipoForm',
        3: 'participanteForm',
        4: 'paisForm',
        5: 'alianzaForm',
        6: 'habilidadForm',
        7: 'reglaForm',
        8: 'desafioForm',
        9: 'rondaEliminacionForm',

    }
    aux = nombre_dict.get(num)
    form = forms_dict.get(num)

    return render(request, "admin/accionAdmin.html", {"aux": aux, 'num': num, 'form': form})


def modificacionAdmin(request, num):
    lista =None
    if num == 1:
        lista = Temporada.objects.all()
    elif num == 2:
        lista =  Equipo.objects.all()
    elif num == 3:
        lista =  Participante.objects.all()
    elif num == 4:
        lista =  Pais.objects.all()
    elif num == 5:
        lista =  Alianza.objects.all()
    elif num == 6:
        lista =  Habilidad.objects.all()
    elif num == 7:
        lista =  Regla.objects.all()
    elif num == 8:
        lista =  Desafio.objects.all()
    elif num == 9:
        lista =  RondaEliminacion.objects.all()
    else:
        return HttpResponse("Error")
    return render(request, "admin/modificacion.html", {"num": num, 'lista': lista})

def modificarForm(request, num):
    if num == 1:
        seleccion_pk = request.GET.get('seleccion')
        objeto_seleccionado = get_object_or_404(Temporada, pk=seleccion_pk)
        print(objeto_seleccionado)
        return render(request, 'forms/temporadaForm.html')
    elif num == 2:
        seleccion_pk = request.GET.get('seleccion')
        objeto_seleccionado = get_object_or_404(Equipo, pk=seleccion_pk)
        print(objeto_seleccionado)
        return render(request, 'forms/equipoForm.html')
    elif num == 3:
        seleccion_pk = request.GET.get('seleccion')
        participante = get_object_or_404(Participante, pk=seleccion_pk)
        print(participante)
        if request.method == 'POST':
            participante.nombre = request.POST.get('nombre')
            participante.apellido = request.POST.get('apellido')
            participante.apodo = request.POST.get('apodo')
            participante.descripcion = request.POST.get('descripcion')
            participante.estado_participacion = request.POST.get('estado_participacion')
            participante.habilidad = request.POST.get('habilidad')
            participante.pais = request.POST.get('pais')
            participante.save()
        return render(request, 'forms/participanteForm.html', {'participante': participante})
    elif num == 4:
        seleccion_pk = request.GET.get('seleccion')
        objeto_seleccionado = get_object_or_404(Pais, pk=seleccion_pk)
        print(objeto_seleccionado)
        return render(request, 'forms/paisForm.html', {'pk': pk})
    elif num == 5:
        seleccion_pk = request.GET.get('seleccion')
        objeto_seleccionado = get_object_or_404(Alianza, pk=seleccion_pk)
        print(objeto_seleccionado)
        return render(request, 'forms/alianzaForm.html', {'pk': pk})
    elif num == 6:
        seleccion_pk = request.GET.get('seleccion')
        objeto_seleccionado = get_object_or_404(Habilidad, pk=seleccion_pk)
        print(objeto_seleccionado)
        return render(request, 'forms/habilidadForm.html', {'pk': pk})
    elif num == 7:
        seleccion_pk = request.GET.get('seleccion')
        objeto_seleccionado = get_object_or_404(Regla, pk=seleccion_pk)
        print(objeto_seleccionado)
        return render(request, 'forms/reglaForm.html', {'pk': pk})
    elif num == 8:
        seleccion_pk = request.GET.get('seleccion')
        objeto_seleccionado = get_object_or_404(Desafio, pk=seleccion_pk)
        print(objeto_seleccionado)
        return render(request, 'forms/desafioForm.html', {'pk': pk})
    elif num == 9:
        seleccion_pk = request.GET.get('seleccion')
        objeto_seleccionado = get_object_or_404(RondaEliminacion, pk=seleccion_pk)
        print(objeto_seleccionado)
        return render(request, 'forms/rondaEliminacionForm.html', {'pk': pk})
    else:
        return HttpResponse("Error")
    