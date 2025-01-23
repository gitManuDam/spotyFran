from django.core.management.base import BaseCommand
from django.db.models import QuerySet

from bdSpotify.models import *
class Command(BaseCommand):
    help = 'Temporal'

    def handle(self, *args, **kwargs):

        try:
            temp = Temporal.objects.all()

            for t in temp:
                album = Album.objects.get(id=t.idAlbum)
                c = Cancion.objects.get(id=t.idCancion)
                c.albumf= album
                c.save()





        except Exception as e :
            self.stderr.write(self.style.ERROR(f'Error: {e}'))


