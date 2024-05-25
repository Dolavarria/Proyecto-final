from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.

class User(AbstractUser):
    rut = models.CharField(max_length=12, unique=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono_personal = models.CharField(max_length=15)
    correo_electronico = models.EmailField(max_length=50)
    tipo_usuario = models.CharField(max_length=15, choices=[('arrendatario', 'Arrendatario'), ('arrendador', 'Arrendador')])

    groups = models.ManyToManyField(Group, blank=True, related_name="customuser_groups")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="customuser_permissions")

    def __str__(self):
        return f"Nombre de usuario: {self.username} \n Rut: {self.rut} \n Nombres: {self.nombres} \n Apellidos: {self.apellidos} \n Direccion: {self.direccion} \n Telefono personal: {self.telefono_personal} \n Correo electronico: {self.correo_electronico} \n Tipo de usuario: {self.tipo_usuario}"
    
class Propiedad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    m2_construidos = models.IntegerField()
    m2_totales = models.IntegerField()
    cantidad_estacionamientos = models.IntegerField()
    cantidad_habitaciones = models.IntegerField()
    cantidad_banos = models.IntegerField()
    direccion = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    tipo_inmueble = models.CharField(max_length=50, choices=[('casa', 'Casa'), ('departamento', 'Departamento'), ('parcela', 'Parcela')])
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
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
'''
Requerimiento 3 (Shell Django)

from Arriendos.models import User,Propiedad,SolicitudArriendo

#Crear objeto con el modelo
new_user = User.objects.create(
    username='diego',
    rut='15341672-1',
    nombres='Diego',
    apellidos='Olavarria',
    direccion='123 Calle falsa',
    telefono_personal='3817291923',
    correo_electronico='diego@example.com',
    tipo_usuario='arrendatario'
)

#Enlistar desde el modelo de datos
all_users = User.objects.all()
for user in all_users:
    print(user)

#Actualizar un registro en el modelo
all_users = User.objects.all()
user = User.objects.get(username='diego')
user.correo_electronico = 'diego.edit@example.com'
user.save()

#Eliminar un registro en el modelo
user = User.objects.get(username='john')
user.delete()

'''
