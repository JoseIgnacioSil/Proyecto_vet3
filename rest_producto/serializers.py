from rest_framework import serializers
from vet.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto','nombreP','descripcion','precio','cantidadInventario','fechaIngreso']