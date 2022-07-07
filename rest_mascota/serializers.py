from rest_framework import serializers
from vet.models import Mascota

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['idMascota','nombre','sexo','color','esterilizado','cliente','imagen']