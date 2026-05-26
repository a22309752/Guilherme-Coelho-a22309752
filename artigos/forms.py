from django import forms
from .models import Comentario, Artigo


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["texto"]

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = [
            "titulo",
            "texto",
            "fotografia",
            "link_externo",
        ]