from django import forms
from django.forms import inlineformset_factory
from .models import Animal, HistorialAlimentacion, Persona

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre', 'especie', 'genero', 'edad']

class HistorialAlimentacionForm(forms.ModelForm):
    class Meta:
        model = HistorialAlimentacion
        fields = ['horario', 'alimentos']

# Inline formset para registrar Historial junto con Animal
HistorialInlineFormSet = inlineformset_factory(
    Animal, HistorialAlimentacion, form=HistorialAlimentacionForm, extra=1, can_delete=True
)
