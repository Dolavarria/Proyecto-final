from django.core.management.base import BaseCommand
from Arriendos.models import Propiedad

class Command(BaseCommand):
    help = 'Exporta las propiedades a un archivo de texto separado por regiones'

    def handle(self, *args, **options):
        # Obtén todas las propiedades y ordena por región
        propiedades = Propiedad.objects.values('nombre', 'descripcion', 'comuna__nombre', 'comuna__region__nombre').order_by('comuna__region__nombre')
        with open('inmuebles_region.txt', 'w') as f:
            
            region_actual = None

            for propiedad in propiedades:
                # Si la región ha cambiado, escribe el nombre de la nueva región
                if propiedad['comuna__region__nombre'] != region_actual:
                    region_actual = propiedad['comuna__region__nombre']
                    f.write(f'\nRegion: {region_actual}\n')

                # Escribe el nombre, la descripción y la comuna de la propiedad
                f.write(f'Nombre: {propiedad["nombre"]}, Descripcion: {propiedad["descripcion"]}, Comuna: {propiedad["comuna__nombre"]}\n')

        self.stdout.write(self.style.SUCCESS('Las propiedades han sido exportadas exitosamente.'))