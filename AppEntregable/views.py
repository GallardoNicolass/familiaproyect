from django.shortcuts import render
from .models import Familia, Familiares2, Familiares3
from django.http import HttpResponse

# Create your views here.


def familia(request):
    familiar1= Familia(nombre="Carlos Ariel", apellido="Gallardo", fecha_nacimiento="1971-05-04", edad=51)
    familiar1.save()
    cadena_texto=f"familia1 guardada: nombre: {familiar1.nombre}, apellido:{familiar1.apellido}, fecha_nacimiento:{familiar1.fecha_nacimiento}, edad: {familiar1.edad}"
    return HttpResponse(cadena_texto)


def familiares2(request):
    familiar2= Familia(nombre="lucila", apellido="gallardo", fecha_nacimiento="2008-05-13", edad=14)
    familiar2.save()
    cadena_texto=f"familiar2 guardada: nombre: {familiar2.nombre}, apellido:{familiar2.apellido}, fecha_nacimiento:{familiar2.fecha_nacimiento}, edad: {familiar2.edad}"
    return HttpResponse(cadena_texto)

def familiares3(request):
    familiar3= Familia(nombre="gabriela", apellido="lucero", fecha_nacimiento="1974-07-27", edad=49)
    familiar3.save()
    cadena_texto=f"familiar3 guardada: nombre: {familiar3.nombre}, apellido:{familiar3.apellido}, fecha_nacimiento:{familiar3.fecha_nacimiento}, edad: {familiar3.edad}"
    return HttpResponse(cadena_texto)

#familiar2= Familia(nombre="gabriela", apellido="Lucero", fecha_nacimiento="1974-07-27", edad=51)
