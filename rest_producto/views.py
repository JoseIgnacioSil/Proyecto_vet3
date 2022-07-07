from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from vet.models import Producto
from rest_producto.serializers import ProductoSerializer


@csrf_exempt
@api_view(['GET','POST'])
def lista_producto(request):
    if request.method == 'GET':
        lista_producto = Producto.objects.all()
        serializer = ProductoSerializer(lista_producto, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET','PUT','DELETE'])
def detalle_producto(request, pro):
    try:
        producto= Producto.objects.get(idProducto = pro)
    except Producto.DoesNotExist:
        return Response(Status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        dataM = JSONParser().parse(request)
        serializer = ProductoSerializer(data=dataM)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
                
        
    
