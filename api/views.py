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

from .models import Doctor, Paciente, HistoriaClinica, VademecumMarca, VademecumGenerico, Receta
from .serializers import DoctorSerializer, PacienteSerializer, HistoriaSerializer, VademecumGenericoSerializer, VademecumMarcaSerializer, RecetaSerializer
from rest_framework.permissions import IsAuthenticated

class PacienteListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class DoctorListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class HistoriasListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaSerializer

class HistoriasRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaSerializer

class RecetaListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

class RecetaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

class VademecumMarcaListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = VademecumMarca.objects.all()
    serializer_class = VademecumMarcaSerializer

class VademecumGenericoListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = VademecumGenerico.objects.all()
    serializer_class = VademecumGenericoSerializer

from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def token(request):
    user = User.objects.create_superuser('token', 'email@example.com', 'ribo1234')
    user.save()
    return render(request, 'home.html')