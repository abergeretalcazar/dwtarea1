
from django.db import models

# Create your models here.
class Equipo(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField()
	logo = models.ImageField(upload_to='img_logo/')
	codigo = models.CharField(max_length=3)
	
	def __str__(self):
		return self.nombre

POSICION_CHOICES = (
	('bs','Base'),
	('es', 'Escolata'),
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
	foografia = models.ImageField(upload_to='img_player')
	posicion = models.CharField(max_length=3, choices=POSICION_CHOICES, default="bs")
	nombre_equipo = models.ForeignKey('Equipo', on_delete = models.CASCADE)
	
	def __str__(self):
		return self.nombre

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
	nombre_equipo = models.ForeignKey('Equipo', on_delete = models.CASCADE)

	def __str__(self):
		return self.nombre