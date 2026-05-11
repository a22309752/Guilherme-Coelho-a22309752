from django.shortcuts import get_object_or_404, redirect, render
from .models import (
    Licenciatura,
    Unidade_Curricular,
    Projeto,
    Tecnologia,
    Formacao,
    MakingOf,
    Competencia, 
    Formacao,
    TFC,
)

def home(request):
    return render(request, )