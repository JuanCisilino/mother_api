from rest_framework import generics

from .models import Pokemon
from .serializers import PokemonSerializer
import requests

class PokemonList(generics.ListCreateAPIView):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()

def init(request):
    try:
        response = requests.get('https://pokeapi.co/api/v2/pokemon?offset=0&limit=1500')

        if response.status_code == 200:
            data = response.json()
            result_list = data['results']
            if Pokemon.objects.count() != len(result_list):
                for pokemon in result_list:
                    pokelocal = Pokemon()
                    pokelocal.name = pokemon['name']
                    pokelocal.base_url = pokemon['url']
                    pokelocal.favorite = False
                    pokelocal.nick_name = ""
                    elemento = pokelocal.base_url.split("/")[-2]
                    pokelocal.id = int(elemento)

                    pokeResponse = requests.get(pokelocal.base_url)
                    pokeData = pokeResponse.json()

                    sprites = pokeData['sprites']
                    pokelocal.list_img = sprites['front_default'] or ""
                    pokelocal.det_img = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/'+str(pokelocal.id)+'.png'

                    type_list = pokeData['types']

                    types = []
                    noDamageTo = []
                    noDamageFrom = []
                    strongAgainst = []
                    weakAgainst = []

                    for type in type_list:
                        tipo = type['type']
                        types.append(tipo['name'])
                        url = tipo['url']

                        typeResponse = requests.get(url)
                        typeData = typeResponse.json()

                        damageRelations = typeData['damage_relations']
                        doubleDamageFrom = damageRelations['double_damage_from']

                        for double in doubleDamageFrom:
                            name = double['name']
                            weakAgainst.append(name)
                        
                        doubleDamageTo = damageRelations['double_damage_to']

                        for double in doubleDamageTo:
                            name = double['name']
                            strongAgainst.append(name)
                        
                        no_damage_from = damageRelations['no_damage_from']

                        for double in no_damage_from:
                            name = double['name']
                            noDamageFrom.append(name)
                        
                        no_damage_to = damageRelations['no_damage_to']

                        for double in no_damage_to:
                            name = double['name']
                            noDamageTo.append(name)
                        
                        pokelocal.types = ";".join(types)
                        pokelocal.strong_against = ";".join(strongAgainst)
                        pokelocal.weak_against = ";".join(weakAgainst)
                        pokelocal.no_damage_from = ";".join(noDamageFrom)
                        pokelocal.no_damage_to = ";".join(noDamageTo)
                    
                    species = pokeData['species']
                    specie_url = species['url']

                    speciesResponse = requests.get(specie_url)
                    specieData = speciesResponse.json()

                    # evolution = specieData['evolution_chain']
                    # evolution_url = evolution['url']

                    # chainResponse = requests.get(evolution_url)
                    # chainData = chainResponse.json()

                    # chain = chainData['chain']
                    # evolvesTo = chain['evolves_to']

                    # for pokes in evolvesTo:
                    #     specie = pokes['species']
                    #     evolvesTo = specie['name']
                    #     if pokelocal.name != evolvesTo:
                    #         pokelocal.evolves_to = evolvesTo
                    #     else:
                    #         pokelocal.evolves_to = ""

                    # evolvesFrom = specieData['evolves_from_species'] or ""
                    # if evolvesFrom != "":
                    #     if evolvesFrom != pokelocal.name:
                    #         pokelocal.evolves_from = evolvesFrom['name']
                    #     else:
                    #         pokelocal.evolves_from = ""
                    # else:
                    #     pokelocal.evolves_from = ""

                    flavors = specieData['flavor_text_entries']
                    flavorList = []

                    for flavor in flavors:
                        text = flavor['flavor_text']
                        language = flavor['language']
                        lan_name = language['name']
                        if lan_name == "es":
                            flavorList.append(text)
                    
                    pokelocal.flavor = ";".join(flavorList)

                    print(pokelocal.id)
                    print(pokelocal.name)
                    pokelocal.save(pokelocal)
                    # print(pokelocal.evolves_from)
                    # print(pokelocal.evolves_to)

            else: 
                print("Up To Date")
        else:
            print("Error en la solicitud. Codigo de estado: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error en la llamada HTTP: {e}")
    return render(request, 'home.html')

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