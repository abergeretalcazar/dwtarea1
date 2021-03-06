from django.contrib import admin

from .models import	Equipo, Jugador, Entrenador, Partido

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
	list_display = ('nombre','thumbnail_logo','descripcion','codigo')
	search_fields = ('nombre','codigo')
	list_filter = ('nombre','codigo')
	fields = ('thumbnail_logo', 'nombre', 'descripcion', 'codigo', 'logo' )
	readonly_fields = ('thumbnail_logo', )

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'thumbnail' ,'apodo', 'fecha_nacimiento', 'edad', 'rut', 'email', 'estatura', 'peso', 'posicion', 'nombre_equipo', 'nombre_partido')	
	search_fields = ('nombre', 'apodo', 'rut')
	list_filter = ('nombre_equipo', 'fecha_nacimiento')
	fields = ('thumbnail', 'nombre', 'apodo', 'fecha_nacimiento', 'edad', 'rut', 'email', 'estatura', 'peso', 'posicion', 'nombre_equipo', 'nombre_partido', 'fotografia')
	readonly_fields = ('thumbnail', )
	
@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre')		

@admin.register(Entrenador)
class EntrenadorAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'edad', 'email', 'rut', 'apodo', 'nombre_equipo')


	# Register your models here.
