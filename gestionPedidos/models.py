from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(("Nombre"), max_length=30)
    direccion=models.CharField(("Dirección"), max_length=50)
    email=models.EmailField(("Email"), blank=True, null=True, max_length=254)
    telefono=models.CharField(("Telefono"), max_length=9)

    def __str__(self):
        return (self.nombre)

class Articulos(models.Model):
    nombre=models.CharField(("Nombre"), max_length=30)
    seccion=models.CharField(("Sección"), max_length=20)
    precio=models.IntegerField(("Precio"))

    def __str__(self):
        return 'El nombre es %s la sección es %s y el precio es %s' %(self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero=models.IntegerField(("Num."))
    fecha=models.DateField(("Fecha"), auto_now=False, auto_now_add=False)
    entregado=models.BooleanField(("Entregado"))
