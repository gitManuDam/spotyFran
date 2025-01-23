from django.core.management.base import BaseCommand
from bdSpotify.models import Cancion

class Command(BaseCommand):
    help = 'Clonar los datos de la columna "idgenero" a la nueva columna "genero"'

    def handle(self, *args, **kwargs):
        # Obtener todas las canciones
        canciones = Cancion.objects.all()

        # Recorrer todas las canciones y copiar los valores de 'idgenero' a 'genero'
        for cancion in canciones:
            if cancion.idgenero:  # Si tiene un valor en 'idgenero'
                cancion.genero = cancion.idgenero  # Copiar el valor de 'idgenero' a 'genero'
                cancion.save()  # Guardar la canción con el nuevo valor

                self.stdout.write(self.style.SUCCESS(f'Canción "{cancion.titulo}" actualizada correctamente.'))

        self.stdout.write(self.style.SUCCESS('Proceso de clonación de géneros completado.'))
