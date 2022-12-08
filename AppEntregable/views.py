from django.shortcuts import render
from .models import Familia, Familiares2, Familiares3
from django.http import HttpResponse
from django.template import Template, context, loader

# Create your views here.


def familia(request):
    familiar1= Familia(nombre="Carlos Ariel", apellido="Gallardo", fecha_nacimiento="1971-05-04", edad=51)
    familiar1.save()
    
    

    familiar2= Familia(nombre="lucila", apellido="gallardo", fecha_nacimiento="2008-05-13", edad=14)
    familiar2.save()
    
    

    familiar3= Familia(nombre="gabriela", apellido="lucero", fecha_nacimiento="1974-07-27", edad=49)
    familiar3.save()
    
    

def plantillarend(request):
    familiares=[
    {"nombre":"Carlos", "apellido":"Gallardo", "fecha_nacimiento":"1971-05-04","edad":51},
    {"nombre":"lucila", "apellido":"Gallardo", "fecha_nacimiento":"2008-05-13", "edad":14},
    {"nombre":"gabriela", "apellido":"lucero", "fecha_nacimiento":"1974-07-27", "edad":49}]

    plantilla = loader.get_template('template.html')

    contexto= {"familiares": familiares}

    return HttpResponse(plantilla.render(contexto, request))


 
