from django.contrib import admin

# Register your models here.

from .models import Integrante, Personaje, Obra, GaleriaObra, Evento, Noticia, Institucion, Multimedia, Galeria, GaleriaInstitucion, Cancion, Video, AjustesPagina

admin.site.register(Integrante)
admin.site.register(Personaje)
admin.site.register(Obra)
admin.site.register(GaleriaObra)
admin.site.register(Evento)
admin.site.register(Noticia)
admin.site.register(Institucion)
admin.site.register(Multimedia)
admin.site.register(Galeria)
admin.site.register(GaleriaInstitucion)
admin.site.register(Cancion)
admin.site.register(Video)
admin.site.register(AjustesPagina)