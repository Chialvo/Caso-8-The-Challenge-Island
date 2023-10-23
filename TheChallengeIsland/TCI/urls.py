from django.urls import path
from . import views

urlpatterns = [
    path("", views.prueba, name="prueba"),
    path("home/", views.home, name="home"),
    path('login/', views.login, name='login'),
    path("pruebaequipos/",views.lista_equipos, name="equipos"),
    path('prueba/', views.prueba, name='prueba'),
    path('temporadas/', views.temporadas, name='temporadas'),
    path('equipos/', views.equipos, name='equipos'),
    path('participantes/', views.participantes, name='participantes'),
]
