# Generated by Django 5.1.4 on 2025-01-22 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdSpotify', '0010_alter_cancion_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancion',
            name='albumF',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='canciones', to='bdSpotify.album'),
        ),
    ]
