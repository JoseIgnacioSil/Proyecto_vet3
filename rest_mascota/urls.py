from django.urls import path
from rest_mascota.views import lista_mascota,detalle_mascota
from rest_mascota.viewsLogin import login

urlpatterns = [
    path('lista_mascota',lista_mascota,name='lista_mascota'),
    path('detalle_mascota/<mas>',detalle_mascota,name='detalle_mascota'),
    path('login',login,name='login'),
]