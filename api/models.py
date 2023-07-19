from django.db import models

class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=3000)
    favorite = models.BooleanField()
    types = models.CharField(max_length=3000)
    # evolves_to = models.CharField(max_length=3000)
    # evolves_from = models.CharField(max_length=3000)
    base_url = models.CharField(max_length=3000)
    list_img = models.CharField(max_length=3000)
    det_img = models.CharField(max_length=3000)
    flavor = models.CharField(max_length=3000)
    strong_against = models.CharField(max_length=3000)
    weak_against = models.CharField(max_length=3000)
    no_damage_to = models.CharField(max_length=3000)
    no_damage_from = models.CharField(max_length=3000)

    def __str__(self):
        return self.name

class Usuario(models.Model):
    email = models.EmailField(primary_key=True)
    nombre = models.CharField(max_length=30)
    rol = models.CharField(max_length=30)
    carrito = models.TextField()
    empresa = models.CharField(max_length=30)

class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.IntegerField()
    image = models.CharField(max_length=300)
    company = models.CharField(max_length=30)
    isActive = models.BooleanField()
    type = models.CharField(max_length=30)

class Doctor(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.TextField(max_length=8)
    matricula = models.PositiveIntegerField()
    firma_url = models.TextField(max_length=200)
    photo_url = models.TextField(max_length=200)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    
class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    dni = models.PositiveIntegerField(primary_key=True)
    dj_url = models.CharField(max_length=200)
    afiliado = models.IntegerField()
    doctor = models.IntegerField()
    descripcion = models.CharField(max_length=600)

class HistoriaClinica(models.Model):
    nombre_pdf = models.CharField(max_length=30)
    dni_paciente = models.PositiveIntegerField()
    doctor = models.IntegerField()
    timestamp = models.PositiveBigIntegerField()
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=600)

class Receta(models.Model):
    nombre_pdf = models.CharField(max_length=30)
    dni_paciente = models.PositiveIntegerField()
    doctor = models.IntegerField()
    timestamp = models.PositiveBigIntegerField()
    descripcion = models.CharField(max_length=600)
    generico = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)

class VademecumGenerico(models.Model):
    nombre = models.CharField(max_length=100)
    doctor = models.PositiveIntegerField()

class VademecumMarca(models.Model):
    nombre = models.CharField(max_length=100)
    doctor = models.PositiveIntegerField()
