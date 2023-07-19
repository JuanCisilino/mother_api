from rest_framework import serializers
from .models import Usuario, Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('__all__')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')

from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('__all__')

from .models import Doctor, Paciente, HistoriaClinica, VademecumGenerico, VademecumMarca, Receta

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('__all__')

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('__all__')

class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = ('__all__')

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = ('__all__')

class VademecumGenericoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VademecumGenerico
        fields = ('__all__')

class VademecumMarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VademecumMarca
        fields = ('__all__')