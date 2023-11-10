from django.urls import path, include
from . import views 
urlpatterns = [ 
    path("", views.home, name="home"), 
    path('login/', views.login, name='login'), 
    path('accounts/', include('django.contrib.auth.urls')), 
    path('logout/', exit, name='exit'),

    path('homeAdmin/', views.homeAdmin, name='homeAdmin'),
    path('accionAdmin/<int:num>/', views.accionAdmin, name='accionAdmin'),

    path('participantes/', views.participantes, name='participantes'),
    path('participante/<int:pk>/', views.participante, name='participante'), 
    path('participanteForm/', views.participanteForm, name='participanteForm'), 
    
    path('equipos/', views.equipos, name='equipos'), path('equipo/<int:pk>/', views.equipo, name='equipo'),
    path('equipoForm/', views.equipoForm, name='equipoForm'),
    
    path('temporadas/', views.temporadas, name='temporadas'), path('temporada/<int:pk>/', views.temporada, name='temporada'), 
    ]
