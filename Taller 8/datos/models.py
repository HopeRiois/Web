from django.db import models
from selection.models import Tipodocumento, Ciudad

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipoDocumento = models.ForeignKey(Tipodocumento, on_delete=models.CASCADE)
    documento = models.IntegerField()    
    fechaNacimiento = models.DateField()
    email = models.EmailField(max_length=200)
    lugarResidencia = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    teléfono = models.IntegerField()
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    confirmarPassword = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f"{self.nombres}-{self.apellidos}"