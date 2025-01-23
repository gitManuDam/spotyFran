from django.core.management.base import BaseCommand
from bdSpotify.models import Cancion, Genero

class Command(BaseCommand):
    help = 'Migrar los géneros desde la columna "genero" en Cancion a la nueva columna "idgenero"'

    def handle(self, *args, **kwargs):
        # Paso 1: Obtener todas las canciones
        canciones = Cancion.objects.all()

        # Paso 2: Recorrer todas las canciones y asignar la clave foránea de "idgenero"
        for cancion in canciones:
            if cancion.genero:  # Si la canción tiene un género
                try:
                    # Buscar el objeto Genero que corresponde al valor de la columna 'genero'
                    genero_obj = Genero.objects.get(nombre=cancion.genero)
                    # Asignar la clave foránea en la nueva columna 'idgenero'
                    cancion.idgenero = genero_obj
                    cancion.save()
                    self.stdout.write(self.style.SUCCESS(f'Canción "{cancion.titulo}" actualizada con género "{cancion.genero}".'))
                except Genero.DoesNotExist:
                    self.stderr.write(self.style.ERROR(f'Género "{cancion.genero}" no encontrado para la canción "{cancion.titulo}".'))

        self.stdout.write(self.style.SUCCESS('Migración de géneros completada exitosamente.'))
