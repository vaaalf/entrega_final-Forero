from django import forms

from accounts.models import Perfil


class PerfilForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Perfil
        fields = ['nombre', 'descripcion', 'link', 'imagen']
        labels = {
            'nombre': 'Dime tu nombre',
            'descripcion': 'Hablame de ti',
            'link': 'Tu red social principal',
            'imagen': 'Ilustra tu perfil',
        }