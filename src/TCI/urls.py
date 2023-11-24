from django.urls import path, include
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ 
    path("", views.home, name="home"), 
    path('login/', views.login, name='login'), 
    path('accounts/', include('django.contrib.auth.urls')), 
    path('logout/', views.exit_tci, name='exit'),
    path('register/', views.register_view, name='register'),


    path('homeAdmin/', views.homeAdmin, name='homeAdmin'),
    path('accionAdmin/<int:num>/', views.accionAdmin, name='accionAdmin'),
    path('modificacionAdmin/<int:num>/', views.modificacionAdmin, name='modificacionAdmin'),
    path('eliminacionAdmin/<int:num>/', views.eliminacionAdmin, name='eliminacionAdmin'),
    path('modificarForm/<int:num>/', views.modificarForm, name='modificarForm'),
    path('eliminarForm/<int:num>/', views.eliminarForm, name='eliminarForm'),

    path('participantes/', views.participantes, name='participantes'),
    path('participante/<int:pk>/', views.participante, name='participante'), 

    
    path('equipos/', views.equipos, name='equipos'), path('equipo/<int:pk>/', views.equipo, name='equipo'),

    
    path('temporadas/', views.temporadas, name='temporadas'), path('temporada/<int:pk>/', views.temporada, name='temporada'), 

    #-----Formularios para crear-----#
    path('temporadaForm/', views.temporadaForm, name='temporadaForm'),
    path('equipoForm/', views.equipoForm, name='equipoForm'),
    path('participanteForm/', views.participanteForm, name='participanteForm'),
    path('paisForm/', views.paisForm, name='paisForm'),
    path('habilidadForm/', views.habilidadForm, name='habilidadForm'),
    path('reglaForm/', views.reglaForm, name='reglaForm'),
    path('alianzaForm/', views.alianzaForm, name='alianzaForm'),
    path('desafioForm/', views.desafioForm, name='desafioForm'),
    path('rondaEliminacionForm/', views.rondaEliminacionForm, name='rondaEliminacionForm'),



    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)