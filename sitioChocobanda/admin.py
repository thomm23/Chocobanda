from django.contrib import admin

# Register your models here.

from .models import Integrante, Personaje, Obra, GaleriaObra, Agenda, Noticia, Institucion, Multimedia, Galeria

admin.site.register(Integrante)
admin.site.register(Personaje)
admin.site.register(Obra)
admin.site.register(GaleriaObra)
admin.site.register(Agenda)
admin.site.register(Noticia)
admin.site.register(Institucion)
admin.site.register(Multimedia)
admin.site.register(Galeria)