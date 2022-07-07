from email.policy import default
from site import USER_SITE
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    nombrecompleto = models.CharField(max_length=50,primary_key=True, verbose_name='nombre')
    numero = models.CharField(max_length=20, verbose_name='numero')
    domicilio = models.CharField(max_length=50,null=True, verbose_name='Domicilio')
    fecha = models.DateTimeField(auto_now=True, verbose_name='fecha')
    
    def __str__(self):
        return self.nombrecompleto
    
    
class Mascota(models.Model):
    idMascota = models.IntegerField(auto_created = True,primary_key=True,verbose_name='Id')
    nombre = models.CharField(max_length=50,verbose_name='nombre')
    sexo = models.CharField(max_length=1,verbose_name='sexo')
    color = models.CharField(max_length=50,verbose_name='color')
    esterilizado = models.BooleanField(default=True, verbose_name='Esterilizado')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="mascotas", null=True)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    
    nombre = models.CharField(max_length=50,verbose_name='nombre')
    descripcion = models.CharField(max_length=100,verbose_name='descripcion')
    precio = models.IntegerField(verbose_name='precio')
    
    
    def __str__(self):
        return self.nombre











