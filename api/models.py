from django.db import models

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
