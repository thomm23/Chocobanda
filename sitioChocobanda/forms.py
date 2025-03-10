from django import forms
from django.core.exceptions import ValidationError
from .models import GaleriaObra

class GaleriaObraForm(forms.ModelForm):
    class Meta:
        model = GaleriaObra
        fields = '__all__'

    def clean_foto(self):
        # Obtener la instancia actual (si existe)
        instance = getattr(self, 'instance', None)
        foto = self.cleaned_data.get('foto')

        # Si la instancia ya tiene una foto y se intenta eliminar
        if instance and instance.foto and not foto:
            raise ValidationError("No se puede eliminar la imagen, elimine el campo completo.")
        
        return foto