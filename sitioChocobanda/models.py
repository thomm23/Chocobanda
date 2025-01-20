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
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre
    

class Obra(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='obras/', null=True, blank=True)
    duracion = models.DurationField()
    personajes = models.ManyToManyField(Personaje, related_name='obras')

    def __str__(self):
        return self.titulo

class Evento(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='eventos')
    lugar = models.CharField(max_length=255)
    fecha = models.DateField()
    integrantes = models.ManyToManyField(Integrante, related_name='eventos')
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
    link = models.URLField(null=True, blank=True)
    foto = models.ImageField(upload_to='instituciones/', null=True, blank=True)

    def __str__(self):
        return self.nombre

# Create your models here.