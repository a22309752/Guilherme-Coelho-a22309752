from django.shortcuts import render, redirect
import requests

from .forms import CampeaoForm


BASE_URL = "https://guilhermeparracha22402027.pw.deisi.ulusofona.pt"
API_KEY = "A_TUA_KEY_AQUI"


def get_headers():
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }


def lista_campeoes_colega(request):
    response = requests.get(
        f"{BASE_URL}/lol/api/campeoes/",
        verify=False
    )

    if response.status_code == 200:
        campeoes = response.json()
    else:
        campeoes = []

    return render(request, "api_colega/campeoes/lista.html", {
        "campeoes": campeoes
    })


def detalhe_campeao_colega(request, campeao_id):
    response = requests.get(
        f"{BASE_URL}/lol/api/campeoes/{campeao_id}/",
        verify=False
    )

    if response.status_code == 200:
        campeao = response.json()
    else:
        campeao = None

    return render(request, "api_colega/campeoes/detalhe.html", {
        "campeao": campeao
    })


def criar_campeao_colega(request):
    if request.method == "POST":
        form = CampeaoForm(request.POST)

        if form.is_valid():
            dados = form.cleaned_data

            response = requests.post(
                f"{BASE_URL}/lol/api/campeoes/",
                json=dados,
                headers=get_headers(),
                verify=False
            )

            if response.status_code in [200, 201]:
                return redirect("lista_campeoes_colega")

            erro = f"Erro ao criar campeão. Código: {response.status_code}. Resposta: {response.text}"
        else:
            erro = "O formulário contém erros."

    else:
        form = CampeaoForm()
        erro = None

    return render(request, "api_colega/campeoes/form.html", {
        "form": form,
        "titulo_pagina": "Criar Campeão",
        "erro": erro
    })


def editar_campeao_colega(request, campeao_id):
    response = requests.get(
        f"{BASE_URL}/lol/api/campeoes/{campeao_id}/",
        verify=False
    )

    if response.status_code == 200:
        campeao = response.json()
    else:
        campeao = None

    if request.method == "POST":
        form = CampeaoForm(request.POST)

        if form.is_valid():
            dados = form.cleaned_data

            response = requests.put(
                f"{BASE_URL}/lol/api/campeoes/{campeao_id}/",
                json=dados,
                headers=get_headers(),
                verify=False
            )

            if response.status_code in [200, 201]:
                return redirect("detalhe_campeao_colega", campeao_id=campeao_id)

            erro = f"Erro ao editar campeão. Código: {response.status_code}. Resposta: {response.text}"
        else:
            erro = "O formulário contém erros."

    else:
        form = CampeaoForm(initial=campeao)
        erro = None

    return render(request, "api_colega/campeoes/form.html", {
        "form": form,
        "titulo_pagina": "Editar Campeão",
        "erro": erro
    })


def apagar_campeao_colega(request, campeao_id):
    response = requests.get(
        f"{BASE_URL}/lol/api/campeoes/{campeao_id}/",
        verify=False
    )

    if response.status_code == 200:
        campeao = response.json()
    else:
        campeao = None

    if request.method == "POST":
        response = requests.delete(
            f"{BASE_URL}/lol/api/campeoes/{campeao_id}/",
            headers=get_headers(),
            verify=False
        )

        if response.status_code in [200, 204]:
            return redirect("lista_campeoes_colega")

        erro = f"Erro ao apagar campeão. Código: {response.status_code}. Resposta: {response.text}"

        return render(request, "api_colega/campeoes/apagar.html", {
            "campeao": campeao,
            "erro": erro
        })

    return render(request, "api_colega/campeoes/apagar.html", {
        "campeao": campeao
    })