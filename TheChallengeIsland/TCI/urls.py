from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.login, name='login'),
    path('prueba/', views.prueba, name='prueba'),
    path('temporadas/', views.temporadas, name='tiempo'),
    path('equipo/', views.equipo, name='equipo'),
]