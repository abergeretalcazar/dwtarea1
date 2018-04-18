
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile

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
	def MakeThumbnail(file):
		img = fotografia.open(file)
		img.thumbnail((128, 128), fotografia.ANTIALIAS)
		thumbnailString = StringIO.StringIO()
		img.save(thumbnailString, 'JPEG')
		newFile = InMemoryUploadedFile(thumbnailString, None, 'temp.jpg', 'image/jpeg', thumbnailString.len, None)
		return newFile

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