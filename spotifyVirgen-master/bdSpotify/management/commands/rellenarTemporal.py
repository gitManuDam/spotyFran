from django.core.management.base import BaseCommand
from django.db.models import QuerySet

from bdSpotify.models import *
class Command(BaseCommand):
    help = 'Planes'

    def handle(self, *args, **kwargs):

        canciones = Cancion.objects.all()

        for c in canciones:
            album= Album.objects.get(nombre=c.album)
            Temporal.objects.create(idAlbum=album.id,idCancion=c.id)

