from django.db import models
from django.utils.safestring import mark_safe
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.
class Equipo(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField()
	logo = models.ImageField(upload_to='img_logo')
	codigo = models.CharField(max_length=3)
	
	def thumbnail_logo(self):
		if  self.nombre:
			return mark_safe('<image src="%s" width="60" height="75" />' % self.logo.url)
		else:
			return ' '
		get_image_tag.short_description = 'Photo'
		#get_image_tag.allow_tags = True #redundant
		get_image_tag.admin_order_field = 'nombre'

POSICION_CHOICES = (
	('bs','Base'),
	('es', 'Escolta'),
	('al', 'Alero'),
	('ap','Ala Pivot'),
	('pv','Pivot'),
)

class Jugador(models.Model):
	nombre = models.CharField(max_length=100)
	apodo = models.CharField(max_length=100)
	fecha_nacimiento = models.DateField()
	edad = models.CharField(max_length=3)
	rut = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	estatura = models.CharField(max_length=4)
	peso = models.CharField(max_length=3)
	fotografia = models.ImageField(upload_to='img_player')
	posicion = models.CharField(max_length=3, choices=POSICION_CHOICES, default="bs")
	nombre_equipo = models.ForeignKey('Equipo', on_delete = models.CASCADE)
	nombre_partido = models.ForeignKey('Partido', on_delete = models.CASCADE)

	#def __str__(self):
	#	return self.nombre
	#def thumbnail(self):
  	#	return u'<img src="%s" />' % (self.fotografia.url)
	
	def thumbnail(self):
		if  self.fotografia:
			return mark_safe('<image src="%s" width="60" height="75" />' % self.fotografia.url)
		else:
			return ' '
		get_image_tag.short_description = 'Photo'
		#get_image_tag.allow_tags = True #redundant
		get_image_tag.admin_order_field = 'name'


class Entrenador(models.Model):
	nombre = models.CharField(max_length=100)
	edad = models.CharField(max_length=3)
	email = models.CharField(max_length=100)
	rut = models.CharField(max_length=100)
	apodo = models.CharField(max_length=100)
	nombre_equipo = models.ForeignKey('Equipo', on_delete = models.CASCADE)

	def __str__(self):
		return self.nombre

class Partido(models.Model):
	nombre = models.CharField(max_length=100)
	
	def __str__(self):
		return self.nombre