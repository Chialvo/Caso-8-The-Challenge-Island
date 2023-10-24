from django.contrib import admin
from .models import *

class AlianzaAdmin(admin.ModelAdmin):
    lista_al = ('nombre', 'descripcion', 'activa')

# Register your models here.

admin.site.register(Temporada)
admin.site.register(Participante)
admin.site.register(Pais)
admin.site.register(Equipo)
admin.site.register(Alianza, AlianzaAdmin)
admin.site.register(Reglas)
admin.site.register(Desafio)
admin.site.register(Habilidad)
admin.site.register(Detalle_desafio)
admin.site.register(RondaEliminacion)

