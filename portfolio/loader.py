
from portfolio.models import *
import json

with open ('jsonfiles/Licenciatura.json') as f:
    licenciaturas = json.load(f)

    for licenciatura, info in licenciaturas.items():
        
        Licenciatura.objects.create(
            nome = licenciatura,
            descricao = info['descricao'],
            duracao = info['duracao'],
            url_pagina_oficial = info['url_pagina_oficial'],
            requisitos = info['requisitos']
        )



lic = Licenciatura.objects.first()

with open ('jsonfiles/UnidadesCurriculares.json') as f:
    ucs = json.load(f)

    for uc, info in ucs.items():
        Unidade_Curricular.objects.create(
            nome = uc,
            ano_curricular = info['ano_curricular'],
            semestre = info['semestre'],
            url_uc = info['url_uc'],
            imagem_url = info['imagem_url'],
            licenciatura = lic
        )


with open ('jsonfiles/TFC.json') as f:
    tfcs = json.load(f)

    for tfc, info in tfcs.items():
        TFC.objects.create(
            titulo = tfc,
            autor = info['autor'],
            resumo = info['resumo'],
            imagem = info['imagem'],
            
        )
