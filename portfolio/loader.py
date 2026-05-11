from portfolio.models import *
import json

with open("data/licenciatura.json") as f:
    licenciaturas = json.load(f)

    for licenciatura, info in licenciaturas.items():

        Licenciatura.objects.create(
            nome = licenciatura,
            formato_curso = info["formato do curso"],
            duracao = info["duração"],
            semestres = info["semestres"],
            creditos = info["créditos"],
            descricao = info["descrição"],
            requisitos = info["requisitos"],
            url_oficial = info["url_pagina_oficial"],
        )

lic = Licenciatura.objects.first()

with open ('data/ucs.json') as f:
    ucs = json.load(f)

    for uc, info in ucs.items():
        Unidade_Curricular.objects.create(
            nome = uc,
            ano_curricular = info['ano_curricular'],
            semestre = info['semestre'],
            url_oficial = info['url_uc'],
            imagem= info['imagem_url'],
            licenciatura = lic
        )


with open ('data/tfcs.json') as f:
    tfcs = json.load(f)

    for tfc, info in tfcs.items():
        TFC.objects.create(
            titulo = tfc,
            autor = info['autor'],
            descricao = info['resumo'],
            imagem = info['imagem'],
            
        )