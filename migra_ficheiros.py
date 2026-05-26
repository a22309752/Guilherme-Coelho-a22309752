import os
from django.core.files import File
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import (
    Projeto,
    Formacao,
    MakingOf,
    Tecnologia,
    Unidade_Curricular,
    TFC
)

from artigos.models import Artigo


def migrar_imagem(obj, campo):
    imagem = getattr(obj, campo)

    if imagem and imagem.name:

        try:
            imagem.open('rb')

            imagem.save(
                os.path.basename(imagem.name),
                File(imagem),
                save=True
            )

            print(f"Migrado: {obj} -> {campo}")

        except Exception as e:
            print(f"Erro em {obj}: {e}")


# Projeto
for obj in Projeto.objects.all():
    migrar_imagem(obj, 'imagem')


# Unidade Curricular
for obj in Unidade_Curricular.objects.all():
    migrar_imagem(obj, 'imagem')


# Tecnologia
for obj in Tecnologia.objects.all():
    migrar_imagem(obj, 'logo_oficial')


# Formação
for obj in Formacao.objects.all():
    migrar_imagem(obj, 'logo_oficial')


# MakingOf
for obj in MakingOf.objects.all():
    migrar_imagem(obj, 'imagem1')
    migrar_imagem(obj, 'imagem2')


# TFC
for obj in TFC.objects.all():
    migrar_imagem(obj, 'imagem')


for obj in Artigo.objects.all():
    migrar_imagem(obj, 'fotografia')