from django import forms


class CampeaoForm(forms.Form):
    nome = forms.CharField(
        label="Nome",
        max_length=100
    )

    titulo = forms.CharField(
        label="Título",
        max_length=150
    )

    descricao = forms.CharField(
        label="Descrição",
        widget=forms.Textarea
    )

    ano_lancamento = forms.IntegerField(
        label="Ano de lançamento",
        min_value=2009
    )

    classe_id = forms.IntegerField(
        label="ID da classe",
        min_value=1
    )