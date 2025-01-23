
from django.core.management.base import BaseCommand
from bdSpotify.models import *

class Command(BaseCommand):
    help = 'Eliminar todos los álbumes de la base de datos'

    def handle(self, *args, **kwargs):


        try:
            Cancion.objects.all().delete()
            Album.objects.all().delete()
        except Exception as e :
            self.stderr.write(self.style.ERROR(f'Error: {e}'))