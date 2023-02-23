from rest_framework import generics

from .models import Usuario, Producto
from .serializers import ProductoSerializer, UsuarioSerializer

class ProductoList(generics.ListCreateAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

class UsuarioList(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')