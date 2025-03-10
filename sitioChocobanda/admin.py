from django.contrib import admin
from django.core.exceptions import ValidationError
from .forms import GaleriaObraForm
from .models import Integrante, Personaje, Obra, GaleriaObra, Evento, Noticia, Institucion, Multimedia, AjustesPagina, ProgramaObra, CancionObra, VideoObra

# Estetica basica del ADMIN
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

# Clase para el Inline de GaleriaObra
class GaleriaObraInline(admin.TabularInline):
    model = GaleriaObra
    form = GaleriaObraForm  # Usar el formulario personalizado
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

@admin.register(AjustesPagina)
class AjustesPaginaAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Deshabilita el botón de agregar si ya existe una instancia
        return not AjustesPagina.objects.exists()

    def change_view(self, request, object_id=None, form_url='', extra_context=None):
        # Redirige a la vista de cambio de la instancia existente
        if not AjustesPagina.objects.exists():
            return super().change_view(request, object_id, form_url, extra_context)
        instance = AjustesPagina.objects.first()
        return super().change_view(request, str(instance.pk), form_url, extra_context)

    def get_object(self, request, object_id, from_field=None):
        # Obtiene la única instancia existente
        if AjustesPagina.objects.exists():
            return AjustesPagina.objects.first()
        return None