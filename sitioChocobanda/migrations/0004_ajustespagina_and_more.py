# Generated by Django 5.1 on 2025-01-25 00:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitioChocobanda', '0003_remove_obra_duracion_remove_obra_personajes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AjustesPagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('historia_chocobanda', models.TextField()),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('youtube_link', models.URLField(blank=True, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('correo_electronico', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='institucion',
            old_name='link',
            new_name='link_institucion',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='integrantes',
        ),
        migrations.AddField(
            model_name='institucion',
            name='impacto_social',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('duracion', models.DurationField()),
                ('archivo', models.FileField(upload_to='canciones/')),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='canciones', to='sitioChocobanda.obra')),
            ],
        ),
        migrations.CreateModel(
            name='GaleriaInstitucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='galeria_instituciones/')),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galeria', to='sitioChocobanda.institucion')),
            ],
        ),
        migrations.CreateModel(
            name='GaleriaObra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='galeria_obra/')),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galeria_obra', to='sitioChocobanda.obra')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('enlace_youtube', models.URLField()),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='sitioChocobanda.obra')),
            ],
        ),
        migrations.DeleteModel(
            name='GaleriaFoto',
        ),
    ]
