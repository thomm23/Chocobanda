from django.db import models
from tinymce.models import HTMLField
from cropperjs.models import CropperImageField
from django.core.exceptions import ValidationError
import re

    
class Integrante(models.Model):
    ESTADO_CHOICES = [
        ('actuales', 'Actual'),
        ('invitados', 'Invitado'),
        ('memorables', 'Memorable'),
    ]
    
    nombre = models.CharField(max_length=255)
    ocupacion = models.CharField(max_length=255, null=True, blank=True)
    foto = CropperImageField(upload_to='integrantes/', null=True, blank=True, aspectratio=1,dimensions=(200, 200))
    descripcion = models.CharField(max_length=1000)
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
    foto = CropperImageField(upload_to='personajes/', null=True, blank=True, aspectratio=16/9,dimensions=(1280, 720))
        
    def __str__(self):
        return self.nombre
    

class Obra(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    foto = CropperImageField(upload_to='obras/', null=True, blank=True, aspectratio=16/9,dimensions=(1280, 720))
    
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
    obra = models.ForeignKey('Obra', related_name='galeria_obra', on_delete=models.CASCADE)
    foto = CropperImageField(upload_to='galeria_obra/', aspectratio=1, dimensions=(1024, 768))  # Campo obligatorio
    descripcion = models.CharField(max_length=255, blank=True, null=True)  # Campo opcional

    def __str__(self):
        return f"Galería de {self.obra.titulo}"

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
    duracion = models.DurationField(null=True, blank=True)
    enlace = models.URLField()  # URLField en lugar de TextField
    obra = models.ForeignKey(Obra, related_name='videos_obra', on_delete=models.CASCADE)

    def clean(self):
        youtube_regex = r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+'
        if not re.match(youtube_regex, self.enlace):
            raise ValidationError("Debes ingresar un enlace válido de YouTube.")

    def get_embed_url(self):
        """Convierte el enlace de YouTube en formato embebido"""
        youtube_id = self.get_youtube_id()  # Obtener solo el ID del video
        if youtube_id:
            return f"https://www.youtube.com/embed/{youtube_id}"
        return self.enlace  # En caso de que no se pueda obtener el ID

    def get_youtube_id(self):
        """Extrae el ID del video de YouTube"""
        if "watch?v=" in self.enlace:
            return self.enlace.split("watch?v=")[1].split("&")[0]  # Solo el ID, sin parámetros adicionales
        elif "youtu.be" in self.enlace:
            return self.enlace.split("youtu.be/")[1].split("?")[0]  # Solo el ID, sin parámetros adicionales
        return None

    def get_thumbnail_url(self):
        """Genera la URL de la miniatura del video"""
        youtube_id = self.get_youtube_id()
        if youtube_id:
            return f"https://img.youtube.com/vi/{youtube_id}/0.jpg"
        return None

    def __str__(self):
        return f"{self.titulo} - {self.obra.titulo}"

class Evento(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='eventos')
    lugar = models.CharField(max_length=255)
    fecha = models.DateField()
    hora = models.TimeField(default='00:00:00')

    def __str__(self):
        return f"{self.obra.titulo} en {self.lugar} el {self.fecha}"

class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    fecha = models.DateField()
    cuerpo = models.TextField()
    foto = CropperImageField(upload_to='novedades/', null=True, blank=True, aspectratio=16/9,dimensions=(1280, 720))

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Novedad"
        verbose_name_plural = "Novedades"  # Define el nombre en plural como "Novedades"

class Institucion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    impacto_social = models.TextField(null=True, blank=True)
    link_institucion = models.URLField(null=True, blank=True)
    foto = CropperImageField(upload_to='instituciones/', null=True, blank=True, aspectratio=1,dimensions=(600, 400))

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Instituciones"  # Define el nombre en plural
    
class AjustesPagina(models.Model):
    historia_chocobanda = models.TextField()  # El texto que se podrá modificar
    instagram_link = models.URLField(null=True, blank=True)  # Enlace a Instagram
    facebook_link = models.URLField(null=True, blank=True)  # Enlace a Facebook
    youtube_link = models.URLField(null=True, blank=True)  # Enlace a YouTube
    telefono = models.CharField(max_length=20, null=True, blank=True)  # Teléfono de contacto
    correo_electronico = models.EmailField(null=True, blank=True)  # Correo electrónico de contacto
    foto_principal = CropperImageField(upload_to='ajustes/', null=True, blank=True, aspectratio=16/9,dimensions=(1280, 720))
    frase_foto_principal = models.CharField(max_length=400, null=True, blank=True)  # Frase obligatoria para la foto principal

    def save(self, *args, **kwargs):
        if not self.pk and AjustesPagina.objects.exists():
            raise ValidationError('Solo puede existir una instancia de AjustesPagina.')
        return super(AjustesPagina, self).save(*args, **kwargs)

    def __str__(self):
        return "Ajustes de la Página"

    class Meta:
        verbose_name = "Ajuste de Página"
        verbose_name_plural = "Ajustes de Página"

