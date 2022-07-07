from django.urls import path
from .views import agregar_producto, contacto, descontar_producto, limpiar_carrito,mascotas,registro,galeria,login,index,agregar_mascota,listado_adopcion,modificar_mascota,eliminar_mascota, restar_producto
agregar_producto,descontar_producto,restar_producto,limpiar_carrito
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns =[
    path('',index,name="index"),
    path('login/',LoginView.as_view(template_name='vet/login.html'),name="login"),
    path('logout/',LoginView.as_view(template_name='vet/logout.html'),name="logout "),
    path('mascotas',mascotas,name="mascotas"),
    path('contacto',contacto,name="contacto"),
    path('registro/',registro,name="registro"),
    path('galeria',galeria,name="galeria"),
    path('agregar_mascota',agregar_mascota,name="agregar_mascota"),
    path('listado_adopcion',listado_adopcion,name="listado_adopcion"),
    path('modificar_mascota/<id>',modificar_mascota,name="modificar_mascota"),
    path('eliminar_mascota/<id>',eliminar_mascota,name="eliminar_mascota"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', descontar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    
]