from django.db import models

# Create your models here.

class Productos(models.Model):
    
    nombre = models.CharField(max_length=40)
    precio = models.CharField(max_length=12)
    descripcion = models.CharField(max_length=500)
    numero_pedido = models.IntegerField()
    cantidad = models.IntegerField()
    fecha_salida = models.DateField()
    pendiente = models.BooleanField()
    entregado = models.BooleanField()
    fecha_entrega = models.DateField()
  
    def __str__(self):
        return self.nombre

class Clientes(models.Model):

    id = models.AutoField(primary_key= True)
    numero_cliente = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)
    cedula = models.CharField(max_length=12)
    telefono = models.CharField(max_length=12)
    producto = models.ForeignKey(Productos, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre