from django.db import models
from django.db.models import Model

# Create your models here.
class  Alumno(Model):
    ApellidoPaterno = models.CharField(max_length=30)
    ApellidoMaterno = models.CharField(max_length=30)
    Nombres = models.CharField(max_length=20)
    FechaNacimiento = models.DateField()
    Sexo  = (("M","Masculino"),("F","Femenino"))
    sexo = models.CharField(max_length=1, choices=Sexo, default="Masculino")

    def NombreCompleto(self):
        cadena = "{0},{1},{2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()
