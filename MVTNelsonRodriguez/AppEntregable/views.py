import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Persona


# Create your views here.


def familia(self):

    persona1 = Persona(nombre="Juan",apellido="Saraza",dni=92568652, fechaNacimiento = datetime.date(1948,11,9))
    persona1.save()
    persona2 = Persona(nombre="Maria",apellido="Malanga",dni=20557542, fechaNacimiento =datetime.date(1952,1,19))
    persona2.save()
    persona3 = Persona(nombre="Roberto",apellido="Carlos",dni=45782356, fechaNacimiento =datetime.date(2000,6,12))
    persona3.save()

    lista = [persona1,persona2,persona3]
    listaPrimera = [persona1.nombre, persona1.apellido, persona1.dni, persona1.fechaNacimiento]
    listaSegunda = [persona2.nombre, persona2.apellido, persona2.dni, persona2.fechaNacimiento]
    listaTercera = [persona3.nombre, persona3.apellido, persona3.dni, persona3.fechaNacimiento]

    """ for persona in lista:
        diccionario = {"nombre":persona.nombre,"apellido":persona.apellido,"dni":persona.dni,"fechanacimiento":persona.fechaNacimiento}
        listaDicci.append(diccionario) """

    dicc = {"uno":listaPrimera,"dos":listaSegunda,"tres":listaTercera}

    plantilla = loader.get_template("plantilla.html")
    
    plantillaRender = plantilla.render(dicc)

    return HttpResponse(plantillaRender)






