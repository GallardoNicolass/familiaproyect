from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse

# Create your views here.


def familia(request):

    familiar1= Familia(nombre="Carlos Ariel", apellido="Gallardo", fecha_nacimiento="1971-05-04", edad=51)
    familiar1.save()
    cadena_texto=f"familia1 guardada: nombre: {familiar1.nombre}, apellido:{familiar1.apellido}, fecha_nacimiento:{familiar1.fecha_nacimiento}, edad: {familiar1.edad}"
    return HttpResponse(cadena_texto)



#familiar2= Familia(nombre="gabriela", apellido="Lucero", fecha_nacimiento="1974-07-27", edad=51)
