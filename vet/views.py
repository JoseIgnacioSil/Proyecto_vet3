from django.shortcuts import render,redirect, HttpResponse
from .forms import MascotaForm, CustomUserCreationForm
from .models import Mascota,Producto
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from vet.models import Producto
from vet.Carrito import Carrito



'''
class Persona:
    def __init__(self,rut,nombre,edad,telefono):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        super().__init__()
        '''
     
# Create your views here.

def index(request):
    productos = Producto.objects.all()
    return render(request, 'vet/index.html', {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("index")

def descontar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("index")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("index")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("index")

def login(request):
    
    return render(request, 'vet/login.html')

def mascotas(request):
    
    return render(request, 'vet/mascotas.html')

def contacto(request):
    
    return render(request, 'vet/contacto.html')  

def galeria(request):
    
    return render(request, 'vet/galeria.html')  

def registro(request):
    data= {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password =formulario.cleaned_data["password1"])
            messages.success(request, 'Usuario {username} creado!')
            login(request)
            
            
            return redirect(to="index")
        data["form"] = formulario
    
    return render(request, 'vet/registration/registro.html', data)  

@permission_required('vet.add_mascota')
def agregar_mascota(request):
    datos = {
        'form' : MascotaForm()
    }

    if (request.method == 'POST'):
        formulario = MascotaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save() #insert
            datos['mensaje'] = "Se registro la mascota"
        else:
            datos['mensaje'] = "Revise datos"
    return render(request,'vet/agregar_mascota.html', datos)
@permission_required('vet.view_mascota')
def listado_adopcion(request):
    mascotas = Mascota.objects.all() #select
    data = {
        'mascotas':mascotas
    }
    return render(request, 'vet/listado_adopcion.html',data)

@permission_required('vet.change_mascota')
def modificar_mascota(request, id):
    mascota = Mascota.objects.get(nombre = id) #select * from Vehiculo where patente = id
    datos = {
        'form' : MascotaForm(instance = mascota)
    }
    
    if (request.method == 'POST'):
        formulario = MascotaForm(data = request.POST, instance = mascota)
        if formulario.is_valid():
            formulario.save() #update
            datos['mensaje'] = "Se modificó la mascota"
        else:
            datos['mensaje'] = "Revise datos, no se modificó"
    return render(request, 'vet/modificar_mascota.html', datos)
@permission_required('vet.delete_mascota')
def eliminar_mascota(request, id):
    mascota = Mascota.objects.get(nombre = id)
    mascota.delete() #delete from Vehiculo where patente = id
    
    return redirect(to='mascotas')



