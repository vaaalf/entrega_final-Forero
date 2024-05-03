from django import forms

from blog.models import Entrada, Comentario


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
        labels = {
            'titulo': 'Dale un titulo a tu entrada',
            'subtitulo': 'Subtitulo',
            'contenido': 'Desborda tus pensamientos',
            'imagen': 'Ilustra tu pensamiento',
        }


class ComentarioForm(forms.ModelForm):
    entrada = forms.ModelChoiceField(queryset=Entrada.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Comentario
        fields = ['mensaje', 'entrada']
        labels = {
            'mensaje': 'Deja un comentario al autor',
        }

class BusquedaForm(forms.Form):
    buscar = forms.CharField(max_length=100, required=True, label="Busca tu inspiración")