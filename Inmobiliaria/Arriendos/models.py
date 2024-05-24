from django.contrib.auth.models import AbstractUser
from django.db import models

#Create your models here.

class User(AbstractUser):
    rut = models.CharField(max_length=12, unique=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direcion = models.CharField(max_length=50)
    telefono_personal = models.CharField(max_length=15)
    correo_electronico = models.EmailField(max_length=50)
    tipo_usuario = models.CharField(max_length=10, choices=[('arrendatario', 'Arrendatario'), ('arrendador', 'Arrendador')])

    def __str__(self):
        return f"{self.username} ({self.tipo_usuario})"
    
class Propiedad(models.Model):
    tipo_propiedad = [
        ('Casa', 'Casa'),
        ('Departamento', 'Departamento'),
        ('Parcela', 'Parcela')
    ]

    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    cantidad_estacionamientos = models.IntegerField()
    cantidad_habitaciones = models.IntegerField()
    cantidad_banos = models.IntegerField()
    direccion = models.CharField(max_length=255)
    comuna = models.CharField(max_length=100)
    tipo_propiedad = models.CharField(max_length=50, choices=tipo_propiedad)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    propietario = models.ForeignKey(User, related_name='properties', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.tipo_propiedad}) - {self.propietario}"