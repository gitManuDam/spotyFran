from django.core.management.base import BaseCommand
from django.db.models import QuerySet

from bdSpotify.models import *
class Command(BaseCommand):
    help = 'Planes'

    def handle(self, *args, **kwargs):


        # Imprimir álbumes únicos
        nombres_albumes = Cancion.objects.values_list('album', flat=True).distinct()
        for nombre in nombres_albumes:
            if nombre:  # Ignorar valores vacíos
                Album.objects.get_or_create(nombre=nombre)

