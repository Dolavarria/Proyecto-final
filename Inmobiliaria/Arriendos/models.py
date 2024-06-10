from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.





class User(AbstractUser):
    rut = models.CharField(max_length=12, unique=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono_personal = models.CharField(max_length=15)
    correo_electronico = models.EmailField(max_length=50,unique=True)
    tipo_usuario = models.CharField(max_length=15, choices=[('arrendatario', 'Arrendatario'), ('arrendador', 'Arrendador')], null=False, blank=False)
    def __str__(self):
        return f"Nombre de usuario: {self.username} \n Rut: {self.rut} \n Nombres: {self.nombres} \n Apellidos: {self.apellidos} \n Direccion: {self.direccion} \n Telefono personal: {self.telefono_personal} \n Correo electronico: {self.correo_electronico} \n Tipo de usuario: {self.tipo_usuario}"
    
class Propiedad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=False, blank=False)
    m2_construidos = models.IntegerField()
    m2_totales = models.IntegerField()
    cantidad_estacionamientos = models.IntegerField()
    cantidad_habitaciones = models.IntegerField()
    cantidad_banos = models.IntegerField()
    direccion = models.CharField(max_length=50)
    tipo_inmueble = models.CharField(max_length=50, choices=[('casa', 'Casa'), ('departamento', 'Departamento'), ('parcela', 'Parcela')])
    precio_mensual = models.IntegerField()
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE, null=False, blank=False)
    propietario = models.ForeignKey(User, related_name='propiedades', on_delete=models.CASCADE)

    def __str__(self):
        return f"Nombre de la propiedad: {self.nombre} \nDescripcion: {self.descripcion} \nM2 construidos: {self.m2_construidos} \nM2 totales: {self.m2_totales} \nCantidad de estacionamientos: {self.cantidad_estacionamientos} \nCantidad de habitaciones: {self.cantidad_habitaciones} \nCantidad de baños: {self.cantidad_banos} \nDireccion: {self.direccion} \nComuna: {self.comuna} \nTipo de inmueble: {self.tipo_inmueble} \nPrecio mensual: {self.precio_mensual} \nPropietario: {self.propietario}"

class SolicitudArriendo(models.Model):
    propiedad=models.ForeignKey(Propiedad,related_name='Solicitudpropiedad',on_delete=models.CASCADE)
    arrendatario=models.ForeignKey(User,related_name='Solicitudarrendatario',on_delete=models.CASCADE)
    fecha_solicitud=models.DateTimeField(auto_now_add=True)
    estado=models.CharField(max_length=50,choices=[('pendiente','Pendiente'),('aceptada','Aceptada'),('rechazada','Rechazada')])

class Region(models.Model):
    id=models.AutoField(primary_key=True, null=False)
    nombre=models.CharField(max_length=100, null=False, blank=False)
    
class Comuna(models.Model):
    id=models.AutoField(primary_key=True, null=False)
    nombre=models.CharField(max_length=250, null=False, blank=False)
    region=models.ForeignKey(Region,related_name='comuna_region',on_delete=models.CASCADE)
