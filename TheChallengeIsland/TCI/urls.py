from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.login, name='login'),
    path('prueba/', views.prueba, name='prueba'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', exit, name='exit'),
    path('participantes/', views.participantes, name='participantes'),
    path('participante/', views.participante, name='participante'),
    path('equipos/', views.equipos, name='equipos'),
    path('equipo/', views.equipo, name='equipo'),
    path('temporadas/', views.temporadas, name='temporadas'),
    path('temporada/', views.temporada, name='temporada')
]
