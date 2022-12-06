from django.db import models

# Create your models here.


class Familia(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    edad=models.IntegerField()



class Familiares2(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    edad=models.IntegerField()



class Familiares3(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    edad=models.IntegerField()

