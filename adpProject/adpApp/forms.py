from django import forms
from .models import Politica

class PoliticaForm(forms.ModelForm):
    class Meta:
        model = Politica
        fields = ['titulo', 'conteudo']