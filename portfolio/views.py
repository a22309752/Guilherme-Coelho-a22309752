from django.shortcuts import render
from .models import (
    Licenciatura,
    Unidade_Curricular,
    Projeto,
    Tecnologia,
    Formacao,
    MakingOf,
    TFC,
)

def home(request):
    return render(request, "portfolio/home.html")

def licenciatura(request):
    licenciaturas = Licenciatura.objects.all()
    ucs = Unidade_Curricular.objects.all()
    formacoes = Formacao.objects.all()

    return render(request, "portfolio/licenciatura.html", {
        "licenciaturas": licenciaturas,
        "ucs": ucs,
        "formacoes": formacoes,
    })

def projetos(request):
    projetos = Projeto.objects.all()

    return render(request, "portfolio/projetos.html", {
        "projetos": projetos,
    })

def tecnologias(request):
    tecnologias = Tecnologia.objects.all()

    return render(request, "portfolio/tecnologias.html", {
        "tecnologias": tecnologias,
    })

def tfc(request):
    tfcs = TFC.objects.all()

    return render(request, "portfolio/tfc.html", {
        "tfcs": tfcs,
    })

def makingof(request):
    makingofs = MakingOf.objects.all()

    return render(request, "portfolio/makingof.html", {
        "makingofs": makingofs,
    })