import datetime
from django.db import models

# Create your models here.

class Persona(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    fechaNacimiento = models.DateField()