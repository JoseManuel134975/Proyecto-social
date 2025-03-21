from django import forms
from .models import Test, Pregunta

class TestForm(forms.ModelForm):
    class Meta:
        model = Test

        fields=['nombre', 'descripcion'] 
        exclude=['usuario']
        widget = {
            'nombre': forms.TextInput(),
            'descripcion': forms.Textarea(),
        }
        
class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta

        fields=['pregunta'] 
        exclude=['usuario']
        widget = {
            'pregunta': forms.TextInput(),
        }

