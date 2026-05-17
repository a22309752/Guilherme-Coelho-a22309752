from django.shortcuts import get_object_or_404, redirect, render

from .models import (
    Licenciatura,
    Unidade_Curricular,
    Projeto,
    Tecnologia,
    Formacao,
    MakingOf,
    Competencia,
    TFC,
)

from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.utils import is_gestor_portfolio

def home(request):
    return render(request, "portfolio/base.html")


def licenciatura(request):
    licenciatura = Licenciatura.objects.prefetch_related("UCs").first()

    return render(request, "portfolio/licenciatura.html", {
        "licenciatura": licenciatura
    })


def projetos(request):
    projetos = Projeto.objects.all()

    return render(request, "portfolio/projetos.html", {
        "projetos": projetos
    })


def formacoes(request):
    formacoes = Formacao.objects.all()

    return render(request, "portfolio/formacoes.html", {
        "formacoes": formacoes
    })


def tecnologias(request):
    tecnologias = Tecnologia.objects.all()

    return render(request, "portfolio/tecnologia.html", {
        "tecnologias": tecnologias
    })


def competencias(request):
    competencias = Competencia.objects.all()

    return render(request, "portfolio/competencias.html", {
        "competencias": competencias
    })


def makingof(request):
    makingofs = MakingOf.objects.all()

    return render(request, "portfolio/makingof.html", {
        "makingofs": makingofs,
    })


def tfc(request):
    tfcs = TFC.objects.all()

    return render(request, "portfolio/tfc.html", {
        "tfcs": tfcs,
    })


def uc(request, uc_id):
    uc = get_object_or_404(Unidade_Curricular, id=uc_id)

    return render(request, "portfolio/ucs.html", {
        "uc": uc
    })

@login_required
@user_passes_test(is_gestor_portfolio)
def novo_projeto(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("portfolio:projetos")

    return render(request, "portfolio/novo_projeto.html", {
        "form": form
    })

@login_required
@user_passes_test(is_gestor_portfolio)
def edita_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)

    form = ProjetoForm(
        request.POST or None,
        request.FILES or None,
        instance=projeto
    )

    if form.is_valid():
        form.save()
        return redirect("portfolio:projetos")

    return render(request, "portfolio/edita_projeto.html", {
        "form": form,
        "projeto": projeto
    })

@login_required
@user_passes_test(is_gestor_portfolio)
def apaga_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)

    if request.method == "POST":
        projeto.delete()
        return redirect("portfolio:projetos")

    return render(request, "portfolio/apaga_projeto.html", {
        "projeto": projeto
    })

@login_required
@user_passes_test(is_gestor_portfolio)
def nova_tecnologia(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("portfolio:tecnologias")

    return render(request, "portfolio/nova_tecnologia.html", {
        "form": form
    })

@login_required
@user_passes_test(is_gestor_portfolio)
def editar_tecnologia(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)

    form = TecnologiaForm(
        request.POST or None,
        request.FILES or None,
        instance=tecnologia
    )

    if form.is_valid():
        form.save()
        return redirect("portfolio:tecnologias")

    return render(request, "portfolio/editar_tecnologia.html", {
        "form": form,
        "tecnologia": tecnologia
    })

@login_required
@user_passes_test(is_gestor_portfolio)
def apagar_tecnologia(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)

    if request.method == "POST":
        tecnologia.delete()
        return redirect("portfolio:tecnologias")

    return render(request, "portfolio/apagar_tecnologia.html", {
        "tecnologia": tecnologia
    })

@login_required
@user_passes_test(is_gestor_portfolio)
def nova_competencia(request):
    form = CompetenciaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("portfolio:competencias")

    return render(request, "portfolio/nova_competencia.html", {
        "form": form
    })

@login_required
@user_passes_test(is_gestor_portfolio)
def editar_competencia(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)

    form = CompetenciaForm(
        request.POST or None,
        instance=competencia
    )

    if form.is_valid():
        form.save()
        return redirect("portfolio:competencias")

    return render(request, "portfolio/editar_competencia.html", {
        "form": form,
        "competencia": competencia
    })

@login_required
@user_passes_test(is_gestor_portfolio)
def apagar_competencia(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)

    if request.method == "POST":
        competencia.delete()
        return redirect("portfolio:competencias")

    return render(request, "portfolio/apagar_competencia.html", {
        "competencia": competencia
    })

@login_required
@user_passes_test(is_gestor_portfolio)
def nova_formacao(request):
    form = FormacaoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("portfolio:formacoes")

    return render(request, "portfolio/nova_formacao.html", {
        "form": form
    })

@login_required
@user_passes_test(is_gestor_portfolio)
def editar_formacao(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)

    form = FormacaoForm(
        request.POST or None,
        request.FILES or None,
        instance=formacao
    )

    if form.is_valid():
        form.save()
        return redirect("portfolio:formacoes")

    return render(request, "portfolio/editar_formacao.html", {
        "form": form,
        "formacao": formacao
    })

@login_required
@user_passes_test(is_gestor_portfolio)
def apagar_formacao(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)

    if request.method == "POST":
        formacao.delete()
        return redirect("portfolio:formacoes")

    return render(request, "portfolio/apagar_formacao.html", {
        "formacao": formacao
    })