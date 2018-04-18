from django.contrib import admin

from .models import	Equipo #, Jugador, Entrenador, Partido

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'descripcion', 'logo', 'codigo')
	
# Register your models here.
