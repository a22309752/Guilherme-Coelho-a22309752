from django.shortcuts import render
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

from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm


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

def competencias(request):
    competencias = Competencia.objects.all()
    return render(request, "portfolio/competencias.html", {
        "competencias": competencias
    })

def formacoes(request):
    formacoes = Formacao.objects.all()
    return render(request, "portfolio/formacoes.html", {
        "formacoes": formacoes
    })

def novo_projeto(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("portfolio:projetos")

    return render(request, "portfolio/form.html", {"form": form})


def editar_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)

    if form.is_valid():
        form.save()
        return redirect("portfolio:projetos")

    return render(request, "portfolio/form.html", {"form": form})


def apagar_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    projeto.delete()
    return redirect("portfolio:projetos")

def nova_tecnologia(request):
    form = TecnologiaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("portfolio:tecnologias")

    return render(request, "portfolio/form.html", {"form": form})


def editar_tecnologia(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    form = TecnologiaForm(request.POST or None, instance=tecnologia)

    if form.is_valid():
        form.save()
        return redirect("portfolio:tecnologias")

    return render(request, "portfolio/form.html", {"form": form})


def apagar_tecnologia(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    tecnologia.delete()
    return redirect("portfolio:tecnologias")

def nova_competencia(request):
    form = CompetenciaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("portfolio:competencias")

    return render(request, "portfolio/form.html", {"form": form})


def editar_competencia(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    form = CompetenciaForm(request.POST or None, instance=competencia)

    if form.is_valid():
        form.save()
        return redirect("portfolio:competencias")

    return render(request, "portfolio/form.html", {"form": form})


def apagar_competencia(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    competencia.delete()
    return redirect("portfolio:competencias")

def nova_formacao(request):
    form = FormacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("portfolio:formacoes")

    return render(request, "portfolio/form.html", {"form": form})


def editar_formacao(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)
    form = FormacaoForm(request.POST or None, instance=formacao)

    if form.is_valid():
        form.save()
        return redirect("portfolio:formacoes")

    return render(request, "portfolio/form.html", {"form": form})


def apagar_formacao(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)
    formacao.delete()
    return redirect("portfolio:formacoes")