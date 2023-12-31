from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from TCI.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q
from .funcionalidades import *
import datetime
from django.contrib.auth.models import User

def home(request):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarTemporada(busqueda)
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
def temporada(request,pk):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarTemporada(busqueda)
        return render(request, 'temporadas.html', {'temporadas': resultado})
    temporada = get_object_or_404(Temporada, pk=pk)
    participantes = temporada.obtener_participantes_temporada()
    participantes = list(set(participantes))
    equipos = temporada.listaEquipo.all()
    rondas = temporada.listaRondasELiminacion()

    return render(request, "detallesTemporada.html", {'temporada': temporada, 'participantes':participantes, 'equipos':equipos, 'rondas':rondas})

@login_required
def equipos(request):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarEquipo(busqueda)
        return render(request, 'equipos.html', {'equipos': resultado})
    equipos = Equipo.objects.all()
    return render(request, "equipos.html", {'equipos': equipos })

@login_required
def equipo(request, pk):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarEquipo(busqueda)
        return render(request, 'equipos.html', {'equipos': resultado})
    equipo = Equipo.objects.get(pk=pk)
    nombre = equipo.nombre
    listaParticipantes = equipo.listarparticipantes()
    listaalianzas = equipo.listaralianza()

    print(listaParticipantes)
    return render(request, "detallesEquipo.html", {'nombre': nombre, 'listaParticipantes': listaParticipantes, 'listaalianzas':listaalianzas})



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
def homeAdmin(request):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarTemporada(busqueda)
        return render(request, 'temporadas.html', {'temporadas': resultado})
    return render(request, "admin/homeAdmin.html")

@login_required
def accionAdmin(request, num):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarTemporada(busqueda)
        return render(request, 'temporadas.html', {'temporadas': resultado})
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

@login_required
def modificacionAdmin(request, num):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarTemporada(busqueda)
        return render(request, 'temporadas.html', {'temporadas': resultado})
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
    print(lista)
    return render(request, "admin/modificacion.html", {"num": num, 'lista': lista})

@login_required
def eliminacionAdmin(request, num):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarTemporada(busqueda)
        return render(request, 'temporadas.html', {'temporadas': resultado})
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
    print(lista)
    return render(request, "admin/eliminacionAdmin.html", {"num": num, 'lista': lista})

@login_required
def modificarForm(request, num):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarTemporada(busqueda)
        return render(request, 'temporadas.html', {'temporadas': resultado})
    objeto_seleccionado = None
    template_name = None
    desafios = Desafio.objects.all()
    participantes = Participante.objects.all()
    equipos = Equipo.objects.all()
    reglas = Regla.objects.all()
    paises = Pais.objects.all()
    habilidades = Habilidad.objects.all()
    alianzas = Alianza.objects.all()
    rondaEliminaciones = RondaEliminacion.objects.all()

    if num == 1:
        objeto_seleccionado = get_object_or_404(Temporada, pk=request.GET.get('seleccion'))
        template_name = 'forms/temporadaForm.html'
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            numero = request.POST.get('numero')
            objeto_seleccionado.nombre = nombre
            objeto_seleccionado.numero = numero
            objeto_seleccionado.save()
            return redirect("modificacionAdmin", num=1)
    elif num == 2:
        equipo = None
        objeto_seleccionado = get_object_or_404(Equipo, pk=request.GET.get('seleccion'))
        template_name = 'forms/equipoForm.html'
        if request.method == 'POST':
            nombre_equipo = request.POST.get('nombre_equipo')
            objeto_seleccionado.nombre = nombre_equipo
            seleccionadosp = request.POST.getlist('seleccionadosp')
            seleccionadosa = request.POST.getlist('seleccionadosa')
            objeto_seleccionado.participantes.clear()
            objeto_seleccionado.alianzas.clear() 
            

            participantes = Participante.objects.all()
            for participante_id in seleccionadosp:
                participante = Participante.objects.get(pk=participante_id)
                objeto_seleccionado.participantes.add(participante)

            alianzas = Alianza.objects.all()
            for alianza_id in seleccionadosa:
                alianza = Alianza.objects.get(pk=alianza_id)
                objeto_seleccionado.alianzas.add(alianza)
            objeto_seleccionado.save()
            return redirect("modificacionAdmin", num=2)
    elif num == 3:
        objeto_seleccionado = get_object_or_404(Participante, pk=request.GET.get('seleccion'))
        template_name = 'forms/participanteForm.html'
        if request.method == 'POST':
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
            
            objeto_seleccionado.nombre = nombre
            objeto_seleccionado.apellido = apellido
            objeto_seleccionado.apodo = apodo
            objeto_seleccionado.descripcion = descripcion
            objeto_seleccionado.estadoParticipacion = estado_participacion
            objeto_seleccionado.habilidad = habilidad
            objeto_seleccionado.pais = pais
            objeto_seleccionado.save()
            return redirect("modificacionAdmin", num=3)
    elif num == 4:
        objeto_seleccionado = get_object_or_404(Pais, pk=request.GET.get('seleccion'))
        template_name = 'forms/paisForm.html'
        if request.method == 'POST':
            nombre_pais = request.POST.get('nombre')
            descripcion_pais = request.POST.get('descripcion')
            objeto_seleccionado.nombre = nombre_pais
            objeto_seleccionado.descripcion = descripcion_pais
            objeto_seleccionado.save()
            return redirect("modificacionAdmin", num=4)
    elif num == 5:
        objeto_seleccionado = get_object_or_404(Alianza, pk=request.GET.get('seleccion'))
        template_name = 'forms/alianzaForm.html'
        if request.method == 'POST':
            nombre_alianza = request.POST.get('nombre')
            descripcion_alianza = request.POST.get('descripcion')
            estado_alianza = request.POST.get('estado')
            objeto_seleccionado.nombre = nombre_alianza
            objeto_seleccionado.descripcion = descripcion_alianza
            objeto_seleccionado.estado = estado_alianza
            objeto_seleccionado.save()
            return redirect("modificacionAdmin", num=5)
    elif num == 6:
        objeto_seleccionado = get_object_or_404(Habilidad, pk=request.GET.get('seleccion'))
        template_name = 'forms/habilidadForm.html'
        if request.method == 'POST':
            nombre_habilidad = request.POST.get('nombre')
            descripcion_habilidad = request.POST.get('descripcion')
            objeto_seleccionado.nombre = nombre_habilidad
            objeto_seleccionado.descripcion = descripcion_habilidad
            objeto_seleccionado.save()
            return redirect("modificacionAdmin", num=6)
    elif num == 7:
        objeto_seleccionado = get_object_or_404(Regla, pk=request.GET.get('seleccion'))
        template_name = 'forms/reglaForm.html'
        if request.method == 'POST':
            nombre_regla = request.POST.get('nombre')
            descripcion_regla = request.POST.get('descripcion')
            objeto_seleccionado.nombre = nombre_regla
            objeto_seleccionado.descripcion = descripcion_regla
            objeto_seleccionado.save()
            return redirect("modificacionAdmin", num=7)
    elif num == 8:
        objeto_seleccionado = get_object_or_404(Desafio, pk=request.GET.get('seleccion'))
        template_name = 'forms/desafioForm.html'
        if request.method == 'POST':
            # Lógica de actualización para Desafío
            nombre_desafio = request.POST.get('nombre')
            descripcion_desafio = request.POST.get('descripcion')
            reglas_desafio = request.POST.getlist('seleccionados')
            objeto_seleccionado.nombre = nombre_desafio
            objeto_seleccionado.descripcion = descripcion_desafio

            objeto_seleccionado.reglas.clear()
            for regla_id in reglas_desafio:
                regla = Regla.objects.get(pk=regla_id)
                objeto_seleccionado.reglas.add(regla)
            objeto_seleccionado.save()
            return redirect("modificacionAdmin", num=8)

    elif num == 9:
        objeto_seleccionado = get_object_or_404(RondaEliminacion, pk=request.GET.get('seleccion'))
        template_name = 'forms/rondaEliminacionForm.html'

        if request.method == 'POST':
            fecha_ronda_eliminacion = request.POST.get('fecha')
            equipo_eliminado_id = request.POST.get('eliminado')
            desafios = request.POST.getlist('desafios')
            objeto_seleccionado.desafios.clear()
            for desafio_id in desafios:
                desafio = Regla.objects.get(pk=desafio_id)
                objeto_seleccionado.reglas.add(desafio)
            try:
                fecha_ronda_eliminacion = datetime.strptime(fecha_ronda_eliminacion, '%Y-%m-%d').date()
            except ValueError:
                return HttpResponse('Fecha inválida. Por favor, ingresa una fecha en el formato correcto.')

            try:
                equipo_eliminado = Equipo.objects.get(pk=equipo_eliminado_id)
            except Equipo.DoesNotExist:
                return HttpResponse('Equipo no encontrado. Por favor, verifica tu selección.')

            objeto_seleccionado.fechaRondaEliminacion = fecha_ronda_eliminacion
            objeto_seleccionado.eliminado = equipo_eliminado
            objeto_seleccionado.save()
            return redirect('modificacionAdmin', num=9)

    else:
        return HttpResponse("Error")

    return render(request, template_name, {'objeto_seleccionado': objeto_seleccionado, 'equipos': equipos,"participantes": participantes, 'reglas': reglas, 'paises': paises, 'habilidades': habilidades, "alianzas": alianzas, "desafios": desafios, "rondaEliminaciones": rondaEliminaciones})

@login_required
def eliminarForm(request, num):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarTemporada(busqueda)
        return render(request, 'temporadas.html', {'temporadas': resultado})
    if num == 1:
        objeto_seleccionado = get_object_or_404(Temporada, pk=request.GET.get('seleccion'))
        objeto_seleccionado.delete()
    elif num == 2:
        objeto_seleccionado = get_object_or_404(Equipo, pk=request.GET.get('seleccion'))
        objeto_seleccionado.delete()
    elif num == 3:
        objeto_seleccionado = get_object_or_404(Participante, pk=request.GET.get('seleccion'))
        objeto_seleccionado.delete()
    elif num == 4:
        objeto_seleccionado = get_object_or_404(Pais, pk=request.GET.get('seleccion'))
        objeto_seleccionado.delete()
    elif num == 5:
        objeto_seleccionado = get_object_or_404(Alianza, pk=request.GET.get('seleccion'))
        objeto_seleccionado.delete()
    elif num == 6:
        objeto_seleccionado = get_object_or_404(Habilidad, pk=request.GET.get('seleccion'))
        objeto_seleccionado.delete()
    elif num == 7:
        objeto_seleccionado = get_object_or_404(Regla, pk=request.GET.get('seleccion'))
        objeto_seleccionado.delete()
    elif num == 8:
        objeto_seleccionado = get_object_or_404(Desafio, pk=request.GET.get('seleccion'))
        objeto_seleccionado.delete()
    elif num == 9:
        objeto_seleccionado = get_object_or_404(RondaEliminacion, pk=request.GET.get('seleccion'))
        objeto_seleccionado.delete()
    else:
        return HttpResponse("Error")
    return redirect('accionAdmin', num=num)
    
@login_required
def temporadaForm(request):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarTemporada(busqueda)
        return render(request, 'temporadas.html', {'temporadas': resultado})
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        numero = request.POST.get('numero')
        seleccionados = request.POST.getlist('seleccionados')
        rondas = request.POST.getlist('rondas')
        print(rondas,"****"*5)
        desafios = request.POST.getlist('desafios')

        equipos_seleccionados = Equipo.objects.filter(pk__in=seleccionados)
        rondas_seleccionadas = RondaEliminacion.objects.filter(pk__in=rondas)
        desafios_seleccionados = Desafio.objects.filter(pk__in=desafios)

        temporada = Temporada(nombre=nombre, numero=numero)
        temporada.save()
        temporada.listaEquipo.add(*equipos_seleccionados)
        temporada.listaRondaEliminacion.add(*rondas_seleccionadas)

        return redirect('temporada', pk=temporada.pk) 

    equipos = Equipo.objects.all()
    desafios = Desafio.objects.all()
    rondas_deliminaciones = RondaEliminacion.objects.all()

    return render(request, 'forms/temporadaForm.html', {'equipos': equipos, 'desafios': desafios, 'rondaEliminaciones': rondas_deliminaciones})

@login_required
def equipoForm(request):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarEquipo(busqueda)
        return render(request, 'equipos.html', {'equipos': resultado})
    equipo = None  # Inicializar equipo con None

    if request.method == 'POST':
        nombre_equipo = request.POST.get('nombre_equipo')
        seleccionadosp = request.POST.getlist('seleccionadosp')
        seleccionadosa = request.POST.getlist('seleccionadosa')
        equipo = Equipo(nombre=nombre_equipo)
        equipo.save()

        participantes = Participante.objects.all()
        for participante_id in seleccionadosp:
            participante = Participante.objects.get(pk=participante_id)
            equipo.participantes.add(participante)
            print("*****")
            print(equipo.participantes)

        alianzas = Alianza.objects.all()
        for alianza_id in seleccionadosa:
            alianza = Alianza.objects.get(pk=alianza_id)
            equipo.alianzas.add(alianza)

        return redirect('equipo', pk=equipo.pk)

    alianzas = Alianza.objects.all()
    participantes = Participante.objects.all()
    return render(request, 'forms/equipoForm.html', {"participantes": participantes, "alianzas": alianzas})

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


@login_required
def paisForm(request):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarTemporada(busqueda)
        return render(request, 'temporadas.html', {'temporadas': resultado})
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        pais = Pais(nombre=nombre)
        pais.save()
        return redirect("accionAdmin", num=4)
    return render(request, 'forms/paisForm.html')


@login_required
def alianzaForm(request):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarTemporada(busqueda)
        return render(request, 'temporadas.html', {'temporadas': resultado})
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        estado = request.POST.get('estado')
        alianza = Alianza(nombre=nombre, descripcion=descripcion, estado=estado)
        alianza.save()
        return redirect("accionAdmin", num=5)
    return render(request, 'forms/alianzaForm.html')


@login_required
def habilidadForm(request):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarTemporada(busqueda)
        return render(request, 'temporadas.html', {'temporadas': resultado})
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        habilidad = Habilidad(nombre=nombre, descripcion=descripcion)
        habilidad.save()
        return redirect("accionAdmin", num=6)
    return render(request, 'forms/habilidadForm.html')

@login_required
def reglaForm(request):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarTemporada(busqueda)
        return render(request, 'temporadas.html', {'temporadas': resultado})
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        regla = Regla(nombre=nombre, descripcion=descripcion)
        regla.save()
        return redirect("accionAdmin", num=7)
    return render(request, 'forms/reglaForm.html')


@login_required
def desafioForm(request):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarTemporada(busqueda)
        return render(request, 'temporadas.html', {'temporadas': resultado})
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')

        # Crear el objeto Desafio antes de agregar reglas
        desafio = Desafio(nombre=nombre, descripcion=descripcion)
        desafio.save()

        seleccionados = request.POST.getlist('seleccionados')
        reglas = Regla.objects.filter(pk__in=seleccionados)
        
        for regla in reglas:
            print(regla.nombre)

        # Agregar las reglas al desafío
        desafio.reglas.add(*reglas)
        desafio.save()

        return redirect("accionAdmin", num=8)

    reglas = Regla.objects.all()
    return render(request, 'forms/desafioForm.html', {'reglas': reglas})


@login_required
def rondaEliminacionForm(request):
    busqueda = request.GET.get('buscador')
    if busqueda:
        resultado = buscarTemporada(busqueda)
        return render(request, 'temporadas.html', {'temporadas': resultado})
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        eliminado = request.POST.get('eliminado')
        desafio = request.POST.get('desafio')
        equipos = Equipo.objects.all()
        desafios = Desafio.objects.all()

        for i in equipos:

            if i.pk == int(eliminado) :
                eliminado = i
                break
        else:
            return HttpResponse('Eliminado no encontrada. Por favor, verifica tu selección.')
        
        for i in desafios:
            if i.pk == int(desafio):
                desafio = i
                break
        else:
            return HttpResponse('Desafio no encontrada. Por favor, verifica tu selección.')
        ronda = RondaEliminacion(fechaRondaEliminacion=fecha, eliminado=eliminado, desafio=desafio)
        ronda.save()
        return redirect("accionAdmin", num=8)
    desafios = Desafio.objects.all()
    equipos = Equipo.objects.all()
    return render(request, 'forms/rondaEliminacionForm.html', {'desafios': desafios , 'equipos': equipos})


def register_view(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html')

    if request.method == 'POST':
        nombre = request.POST.get('name')
        mail = request.POST.get('email')
        password = request.POST.get('password')      

        user = User.objects.create_user(username=nombre, email=mail, password=password)        
        return redirect('login')