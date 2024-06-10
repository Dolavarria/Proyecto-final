from django.core.management.base import BaseCommand
from Arriendos.models import Propiedad

class Command(BaseCommand):
    help = 'Exporta las propiedades a un archivo de texto'

    def handle(self, *args, **options):
        propiedades = Propiedad.objects.values('nombre', 'descripcion', 'comuna__nombre').order_by('comuna__nombre')
        with open('inmuebles_comuna.txt', 'w') as f:
            
            comuna_actual = None

            for propiedad in propiedades:
                # Si la comuna ha cambiado, escribe el nombre de la nueva comuna
                if propiedad['comuna__nombre'] != comuna_actual:
                    comuna_actual = propiedad['comuna__nombre']
                    f.write(f'\nComuna: {comuna_actual}\n')

                # Escribe el nombre y la descripción de la propiedad
                f.write(f'Nombre: {propiedad["nombre"]}, Descripcion: {propiedad["descripcion"]}\n')

        self.stdout.write(self.style.SUCCESS('Las propiedades han sido exportadas exitosamente.'))