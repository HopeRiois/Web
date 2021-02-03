from django.db import models

class Tipodocumento(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=200)
	def __str__(self):
		return f"{self.nombre}-{self.descripcion}"

class Ciudad(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=200)
	def __str__(self):
		return f"{self.nombre}"