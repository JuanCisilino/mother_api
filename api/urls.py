from django.urls import path
from .views import ProductoList, UsuarioList, ProductoDetail, UsuarioDetail, home, token
from .views import PokemonList, init
from .views import PacienteListCreate, PacienteRetrieveUpdateDestroy, DoctorListCreate, DoctorRetrieveUpdateDestroy, HistoriasListCreate, HistoriasRetrieveUpdateDestroy, VademecumMarcaListCreate, VademecumGenericoListCreate, RecetaListCreate, RecetaRetrieveUpdateDestroy

urlpatterns = [
    path('pokeapi/init', init, name='Home'),
    path('pokeapi/list', PokemonList.as_view()),
    path('wmapi/initProducts/',ProductoList.as_view()),
    path('wmapi/initUsers/',UsuarioList.as_view()),
    path('wmapi/users/<str:pk>',UsuarioDetail.as_view()),
    path('wmapi/prodById/<int:pk>',ProductoDetail.as_view()),
    path('medicapi/pacientes/', PacienteListCreate.as_view(), name='Lista de Pacientes'),
    path('medicapi/doctores/', DoctorListCreate.as_view(), name='Lista de Doctores'),
    path('medicapi/recetas/', RecetaListCreate.as_view(), name='Lista de Recetas'),
    path('medicapi/historias/', HistoriasListCreate.as_view(), name='Lista de Historias Clinicas'),
    path('medicapi/receta/<int:pk>/', RecetaRetrieveUpdateDestroy.as_view(), name='Receta por ID'),
    path('medicapi/historias/<int:pk>/', HistoriasRetrieveUpdateDestroy.as_view(), name='Historia clinica por ID'),
    path('medicapi/paciente/<int:pk>/', PacienteRetrieveUpdateDestroy.as_view(), name='Paciente por DNI'),
    path('medicapi/doctor/<str:pk>/', DoctorRetrieveUpdateDestroy.as_view(), name='Doctor por Email'),
    path('medicapi/vademecum_marca/', VademecumMarcaListCreate.as_view(), name='Lista de Vademecum Marca'),
    path('medicapi/vademecum_generico/', VademecumGenericoListCreate.as_view(), name='Lista de Vademecum Generico'),
    path('api/', token, name='Creacion de usuario token'),
    path('', home, name='Home'),
]