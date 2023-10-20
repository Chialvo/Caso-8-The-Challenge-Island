from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.login, name='login'),
<<<<<<< HEAD
    path("equipos/",views.lista_equipos, name="equipos")
=======
    path('prueba/', views.prueba, name='prueba'),
    path('temporadas/', views.temporadas, name='tiempo'),
    path('equipo/', views.equipo, name='equipo'),
>>>>>>> dad438aaa939acd703e7b89d790b5e03da74fe30
]