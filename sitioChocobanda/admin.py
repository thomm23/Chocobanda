from django.contrib import admin

# Register your models here.

from .models import Integrante, Personaje, Obra, Evento, Noticia, Institucion, Multimedia, Galeria

admin.site.register(Integrante)
admin.site.register(Personaje)
admin.site.register(Obra)
admin.site.register(Evento)
admin.site.register(Noticia)
admin.site.register(Institucion)
admin.site.register(Multimedia)
admin.site.register(Galeria)