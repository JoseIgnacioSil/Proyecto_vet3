from django.urls import path
from rest_producto.views import lista_producto,detalle_producto

urlpatterns = [
    path('lista_producto',lista_producto,name='lista_producto'),
    path('detalle_producto/<pro>',detalle_producto,name='detalle_producto'),
]
