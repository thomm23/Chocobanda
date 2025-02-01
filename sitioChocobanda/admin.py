from django.contrib import admin
from .models import Integrante, Personaje, Obra, GaleriaObra, Evento, Noticia, Institucion, Multimedia, Galeria, Cancion, Video, AjustesPagina, ProgramaObra

# Registrar los modelos en el admin
admin.site.register(Integrante)
admin.site.register(Personaje)
admin.site.register(Evento)
admin.site.register(Noticia)
admin.site.register(Institucion)
admin.site.register(Multimedia)
admin.site.register(Galeria)
admin.site.register(Cancion)
admin.site.register(Video)
admin.site.register(AjustesPagina)

# Clase para el Inline de GaleriaObra
class GaleriaObraInline(admin.TabularInline):
    model = GaleriaObra
    extra = 1
    fields = ['foto', 'descripcion']
    verbose_name = "Imagen de la galería"
    verbose_name_plural = "Galería de la obra"

# Clase para el Inline de ProgramaObra
class ProgramaObraInline(admin.StackedInline):  # O admin.TabularInline
    model = ProgramaObra
    extra = 1
    fields = ['programa']
    verbose_name = "Programa de la obra"
    verbose_name_plural = "Programas de la obra"

# Registrar el modelo Obra con su clase personalizada de admin
@admin.register(Obra)
class ObraAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion')
    search_fields = ('titulo',)
    inlines = [GaleriaObraInline, ProgramaObraInline]  # Agrega ambos inlines aquí