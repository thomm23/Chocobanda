from django.contrib import admin
from .models import Integrante, Personaje, Obra, GaleriaObra, Evento, Noticia, Institucion, Multimedia, AjustesPagina, ProgramaObra, CancionObra, VideoObra

#Estetica basica del ADMIN

admin.site.site_header = "Administración de la Chocobanda"
admin.site.site_title = "Chocobanda | Panel administrativo"
admin.site.index_title = "Bienvenido al panel administrativo de la Chocobanda"



# Registrar los modelos en el admin
admin.site.register(Integrante)
admin.site.register(Personaje)
admin.site.register(Evento)
admin.site.register(Noticia)
admin.site.register(Institucion)
admin.site.register(Multimedia)
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
    verbose_name_plural = "Programa de la obra"

    # Clase para el Inline de CancionObra
class CancionObraInline(admin.StackedInline):  # O admin.TabularInline
    model = CancionObra
    extra = 1
    fields = ['titulo', 'duracion', 'archivo', 'enlace']
    verbose_name = "Canción de la obra"
    verbose_name_plural = "Canciones de la obra"

    # Clase para el Inline de VideoObra
class VideoObraInline(admin.StackedInline):  # O admin.TabularInline
    model = VideoObra
    extra = 1
    fields = ['titulo', 'duracion', 'enlace']
    verbose_name = "Video de la obra"
    verbose_name_plural = "Videos de la obra"

# Registrar el modelo Obra con su clase personalizada de admin
@admin.register(Obra)
class ObraAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion')
    search_fields = ('titulo',)
    inlines = [GaleriaObraInline, ProgramaObraInline, CancionObraInline, VideoObraInline]  # Agrega ambos inlines aquí