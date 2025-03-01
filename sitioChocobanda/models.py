from django.db import models
from tinymce.models import HTMLField
from cropperjs.models import CropperImageField
from django.core.exceptions import ValidationError


class Multimedia(models.Model):
    nombre = models.CharField(max_length=255)
    fecha = models.DateField()
    evento = models.CharField(max_length=255, null=True, blank=True)
    etiquetas = models.TextField(null=True, blank=True)  # JSON or comma-separated
    archivo = models.FileField(upload_to='multimedia/')

class Galeria(models.Model):
    fotos = models.ManyToManyField(Multimedia, related_name='galerias_fotos', blank=True)
    canciones = models.TextField(null=True, blank=True)  # Comma-separated links
    videos = models.ManyToManyField(Multimedia, related_name='galerias_videos', blank=True)
    
class Integrante(models.Model):
    ESTADO_CHOICES = [
        ('actuales', 'Actual'),
        ('invitados', 'Invitado'),
        ('memorables', 'Memorable'),
    ]
    
    nombre = models.CharField(max_length=255)
    ocupacion = models.CharField(max_length=255, null=True, blank=True)
    foto = CropperImageField(upload_to='integrantes/', null=True, blank=True, aspectratio=1,dimensions=(200, 200))
    descripcion = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=255, choices=ESTADO_CHOICES, default='Actual')

    def __str__(self):
        return self.nombre


class Personaje(models.Model):
    nombre = models.CharField(max_length=255)
    integrante = models.ForeignKey(
        "Integrante",
        on_delete=models.CASCADE,
        related_name="personajes"
    )
    foto = CropperImageField(upload_to='personajes/', null=True, blank=True, aspectratio=1,dimensions=(300, 200))
        
    def __str__(self):
        return self.nombre
    

class Obra(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    foto = CropperImageField(upload_to='obras/', null=True, blank=True, aspectratio=1,dimensions=(900, 600))
    
    def __str__(self):
        return self.titulo
    
class ProgramaObra(models.Model):
    obra = models.OneToOneField(
        Obra, 
        on_delete=models.CASCADE, 
        related_name='programa_obra',  # Nombre para acceder desde Obra
        primary_key=True  # Asegura que sea una relación uno a uno
    )
    programa = HTMLField()  # Campo para almacenar el programa de la obra

    def __str__(self):
        return f"Programa de {self.obra.titulo}"

class GaleriaObra(models.Model):
    obra = models.ForeignKey(Obra, related_name='galeria_obra', on_delete=models.CASCADE)
    foto = CropperImageField(upload_to='galeria_obra/', null=True, blank=True, aspectratio=1,dimensions=(1024, 768))
    descripcion = models.CharField(max_length=255, blank=True, null=True)

class CancionObra(models.Model):
    titulo = models.CharField(max_length=255)
    duracion = models.DurationField(null=True, blank=True)  # Opcional si no se conoce la duración
    archivo = models.FileField(upload_to='canciones/', null=True, blank=True)  # Archivo subido
    enlace = models.URLField(null=True, blank=True)  # Enlace externo
    obra = models.ForeignKey(Obra, related_name='canciones_obra', on_delete=models.CASCADE)  # Relación con la obra

    def clean(self):
        if not self.archivo and not self.enlace:
            raise ValidationError("Debes proporcionar un archivo o un enlace para la canción.")
        if self.archivo and self.enlace:
            raise ValidationError("No puedes cargar un archivo y un enlace al mismo tiempo.")
    
    def __str__(self):
        return f"Cancion de {self.obra.titulo}"
    
class VideoObra(models.Model):
    titulo = models.CharField(max_length=255)
    duracion = models.DurationField(null=True, blank=True)  # Opcional si no se conoce la duración
    enlace = models.URLField(null=False, blank=False)  # Enlace Obligatorio
    obra = models.ForeignKey(Obra, related_name='videos_obra', on_delete=models.CASCADE)  # Relación con la obra
    
    def __str__(self):
        return f"Video de {self.obra.titulo}"

class Evento(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='eventos')
    lugar = models.CharField(max_length=255)
    fecha = models.DateField()
    hora = models.TimeField(default='00:00:00')
    invitados = models.TextField(null=True, blank=True)  # JSON or comma-separated
    instituciones_beneficiadas = models.TextField(null=True, blank=True)  # JSON or comma-separated

    def __str__(self):
        return f"{self.obra.titulo} en {self.lugar} el {self.fecha}"

class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    fecha = models.DateField()
    cuerpo = models.TextField()
    foto = CropperImageField(upload_to='novedades/', null=True, blank=True, aspectratio=1,dimensions=(600, 400))

    def __str__(self):
        return self.titulo

class Institucion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    impacto_social = models.TextField(null=True, blank=True)
    link_institucion = models.URLField(null=True, blank=True)
    foto = CropperImageField(upload_to='instituciones/', null=True, blank=True, aspectratio=1,dimensions=(600, 400))

    def __str__(self):
        return self.nombre
    
class AjustesPagina(models.Model):
    historia_chocobanda = models.TextField()  # El texto que se podrá modificar
    instagram_link = models.URLField(null=True, blank=True)  # Enlace a Instagram
    facebook_link = models.URLField(null=True, blank=True)  # Enlace a Facebook
    youtube_link = models.URLField(null=True, blank=True)  # Enlace a YouTube
    telefono = models.CharField(max_length=20, null=True, blank=True)  # Teléfono de contacto
    correo_electronico = models.EmailField(null=True, blank=True)  # Correo electrónico de contacto

    def __str__(self):
        return "Ajustes de la Página"

