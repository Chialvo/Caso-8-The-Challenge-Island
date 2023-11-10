from django.urls import path, include
from . import views 
urlpatterns = [ 
    path("", views.home, name="home"), 
    path('login/', views.login, name='login'), 
    path('accounts/', include('django.contrib.auth.urls')), 
    path('logout/', views.exit_tci, name='exit'),

    path('homeAdmin/', views.homeAdmin, name='homeAdmin'),
    path('accionAdmin/<int:num>/', views.accionAdmin, name='accionAdmin'),
    path('modificacionAdmin/<int:num>/', views.modificacionAdmin, name='modificacionAdmin'),
    path('modificarForm/<int:num>/<int:pk>/', views.modificarForm, name='modificarForm'),

    path('participantes/', views.participantes, name='participantes'),
    path('participante/<int:pk>/', views.participante, name='participante'), 

    
    path('equipos/', views.equipos, name='equipos'), path('equipo/<int:pk>/', views.equipo, name='equipo'),

    
    path('temporadas/', views.temporadas, name='temporadas'), path('temporada/<int:pk>/', views.temporada, name='temporada'), 

    #-----Formularios para crear-----#
    path('temporadaForm/', views.temporadaForm, name='temporadaForm'),
    path('equipoForm/', views.equipoForm, name='equipoForm'),
    path('participanteForm/', views.participanteForm, name='participanteForm'), 

    ]
