from django.db import models

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
    foto = models.ImageField(upload_to='integrantes/', null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=255, choices=ESTADO_CHOICES, default='Actual')

    def __str__(self):
        return self.nombre


class Personaje(models.Model):
    nombre = models.CharField(max_length=255)
    integrante = models.ForeignKey(
        Integrante, 
        on_delete=models.CASCADE, 
        related_name='personajes'
    )  # Relación "uno a muchos"
    foto = models.ImageField(upload_to='personajes/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    

class Obra(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='obras/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class GaleriaObra(models.Model):
    obra = models.ForeignKey(Obra, related_name='galeria_obra', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='galeria_obra/')
    descripcion = models.CharField(max_length=255, blank=True, null=True)

class Evento(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='eventos')
    lugar = models.CharField(max_length=255)
    fecha = models.DateField()
    invitados = models.TextField(null=True, blank=True)  # JSON or comma-separated
    instituciones_beneficiadas = models.TextField(null=True, blank=True)  # JSON or comma-separated

    def __str__(self):
        return f"{self.obra.titulo} en {self.lugar} el {self.fecha}"

class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    fecha = models.DateField()
    cuerpo = models.TextField()
    fotos = models.ManyToManyField(Multimedia, related_name='noticias_fotos', blank=True)

    def __str__(self):
        return self.titulo

class Institucion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    impacto_social = models.TextField(null=True, blank=True)
    link_institucion = models.URLField(null=True, blank=True)
    foto = models.ImageField(upload_to='instituciones/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class GaleriaInstitucion(models.Model):
    institucion = models.ForeignKey(Institucion, related_name='galeria', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='galeria_instituciones/')
    descripcion = models.CharField(max_length=255, blank=True, null=True)

class Cancion(models.Model):
    nombre = models.CharField(max_length=255)
    duracion = models.DurationField()  # Para almacenar la duración en formato HH:MM:SS
    archivo = models.FileField(upload_to='canciones/')  # Subir el archivo de la canción
    obra = models.ForeignKey(Obra, related_name='canciones', on_delete=models.CASCADE)  # Relación con la obra

    def __str__(self):
        return self.nombre
    
class Video(models.Model):
    nombre = models.CharField(max_length=255)
    enlace_youtube = models.URLField()
    obra = models.ForeignKey(Obra, related_name='videos', on_delete=models.CASCADE)  # Relación con la obra

    def __str__(self):
        return f'{self.nombre} - {self.obra.nombre}'
    
class AjustesPagina(models.Model):
    historia_chocobanda = models.TextField()  # El texto que se podrá modificar
    instagram_link = models.URLField(null=True, blank=True)  # Enlace a Instagram
    facebook_link = models.URLField(null=True, blank=True)  # Enlace a Facebook
    youtube_link = models.URLField(null=True, blank=True)  # Enlace a YouTube
    telefono = models.CharField(max_length=20, null=True, blank=True)  # Teléfono de contacto
    correo_electronico = models.EmailField(null=True, blank=True)  # Correo electrónico de contacto

    def __str__(self):
        return "Ajustes de la Página"

# Create your models here.