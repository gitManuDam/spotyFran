# Generated by Django 5.1.4 on 2025-01-23 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdSpotify', '0012_rename_albumf_cancion_albumf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temporal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idAlbum', models.IntegerField()),
                ('idCancion', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='cancion',
            name='albumf',
        ),
    ]
