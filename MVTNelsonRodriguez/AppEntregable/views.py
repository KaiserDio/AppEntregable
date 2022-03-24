import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Persona


# Create your views here.


def familia(self):

    persona1 = Persona(nombre="Juan",apellido="Berna",dni=92568652, fechaNacimiento = datetime.date(1948,11,9))
    persona1.save()
    persona2 = Persona(nombre="Maria",apellido="Obertti",dni=20557542, fechaNacimiento =datetime.date(1952,1,19))
    persona2.save()
    persona3 = Persona(nombre="German",apellido="Berna",dni=45782356, fechaNacimiento =datetime.date(2000,6,12))
    persona3.save()

    lista = [persona1,persona2,persona3]
    listaDicci = []

    for persona in lista:
        diccionario = {"nombre":persona.nombre,"apellido":persona.apellido,"dni":persona.dni,"fechanacimiento":persona.fechaNacimiento}
        listaDicci.append(diccionario)

    dicc = {"ListaFamiliar":listaDicci}

    plantilla = loader.get_template("plantilla.html")
    
    plantillaRender = plantilla.render(dicc)

    return HttpResponse(plantillaRender)






