from ninja import NinjaAPI
from ninja import NinjaAPI
from typing import List
from django.shortcuts import get_object_or_404

from .models import Faccao, Planeta, Personagem, Missao
from .schemas import (
    ErrorSchema,
    FaccaoIn,
    FaccaoOut,
    PlanetaIn,
    PlanetaOut,
    PersonagemIn,
    PersonagemOut,
    MissaoIn,
    MissaoOut,
)


api = NinjaAPI(
    title = "API RESTful do Holocron",
    description = """API para gerir toda a informação contida dentro do Holocron""",
    version = "1.0.0"
)

@api.get("faccao/", response={200: List[FaccaoOut]})
def list_faccao(request):
    faccao = Faccao.objects.all()
    return 200, faccao

@api.get("faccao/{faccao_id}/", response={200: FaccaoOut, 404: ErrorSchema})
def get_faccao(request, faccao_id: int):
    faccao = get_orbject_or_404(Faccao, id=faccao_id)
    return 200, faccao

@api.post("faccao/", response={201: FaccaoOut, 400: ErrorSchema})
def post_faccao(request, data: FaccaoIn):
    faccao = Faccao.objects.create(**data.dict())
    return 201, faccao

@api.put("faccao/{faccao_id}/", response ={200: FaccaoOut, 404: ErrorSchema})
def put_faccao(request, faccao_id: int, data:FaccaoIn):
    faccao = get_object_or_404(Faccao, id = faccao_id)

    for attr, value in data.dict().items():
        settattr(faccao, attr, value)

    faccao.save()
    return 200, faccao

@api.delete("faccao/{faccao_id}/", response={204: None, 404: ErrorSchema})
def delete_faccao(request, faccao_id:int):
    faccao = get_object_or_404(Faccao, id = faccao_id)
    faccao.delete()
    return 204, None



@api.get("planetas/", response={200: List[PlanetaOut]}, tags=["Planetas"])
def list_planetas(request):
    planetas = Planeta.objects.select_related("faccao_controladora").all()
    return 200, planetas

@api.get("planetas/{planeta_id}/", response={200: PlanetaOut, 404: ErrorSchema}, tags=["Planetas"])
def get_planeta(request, planeta_id: int):
    planeta = get_object_or_404(
        Planeta.objects.select_related("faccao_controladora"),
        id=planeta_id
    )
    return 200, planeta

@api.post("planetas/", response={201: PlanetaOut, 400: ErrorSchema}, tags=["Planetas"])
def post_planeta(request, data: PlanetaIn):
    if data.faccao_controladora_id is not None:
        if not Faccao.objects.filter(id=data.faccao_controladora_id).exists():
            return 400, {"detail": "A fação controladora indicada não existe."}

    planeta = Planeta.objects.create(**data.dict())
    return 201, planeta

@api.put("planetas/{planeta_id}/", response={200: PlanetaOut, 400: ErrorSchema, 404: ErrorSchema}, tags=["Planetas"])
def put_planeta(request, planeta_id: int, data: PlanetaIn):
    planeta = get_object_or_404(Planeta, id=planeta_id)

    if data.faccao_controladora_id is not None:
        if not Faccao.objects.filter(id=data.faccao_controladora_id).exists():
            return 400, {"detail": "A fação controladora indicada não existe."}

    for attr, value in data.dict().items():
        setattr(planeta, attr, value)

    planeta.save()
    return 200, planeta

@api.delete("planetas/{planeta_id}/", response={204: None, 404: ErrorSchema}, tags=["Planetas"])
def delete_planeta(request, planeta_id: int):
    planeta = get_object_or_404(Planeta, id=planeta_id)
    planeta.delete()
    return 204, None



@api.get("personagens/", response={200: List[PersonagemOut]}, tags=["Personagens"])
def list_personagens(request):
    personagens = Personagem.objects.select_related(
        "planeta_origem",
        "faccao"
    ).all()

    return 200, personagens

@api.get("personagens/{personagem_id}/", response={200: PersonagemOut, 404: ErrorSchema}, tags=["Personagens"])
def get_personagem(request, personagem_id: int):
    personagem = get_object_or_404(
        Personagem.objects.select_related("planeta_origem", "faccao"),
        id=personagem_id
    )

    return 200, personagem

@api.post("personagens/", response={201: PersonagemOut, 400: ErrorSchema}, tags=["Personagens"])
def post_personagem(request, data: PersonagemIn):
    if not Planeta.objects.filter(id=data.planeta_origem_id).exists():
        return 400, {"detail": "O planeta de origem indicado não existe."}

    if not Faccao.objects.filter(id=data.faccao_id).exists():
        return 400, {"detail": "A fação indicada não existe."}

    personagem = Personagem.objects.create(**data.dict())
    return 201, personagem

@api.put("personagens/{personagem_id}/", response={200: PersonagemOut, 400: ErrorSchema, 404: ErrorSchema}, tags=["Personagens"])
def put_personagem(request, personagem_id: int, data: PersonagemIn):
    personagem = get_object_or_404(Personagem, id=personagem_id)

    if not Planeta.objects.filter(id=data.planeta_origem_id).exists():
        return 400, {"detail": "O planeta de origem indicado não existe."}

    if not Faccao.objects.filter(id=data.faccao_id).exists():
        return 400, {"detail": "A fação indicada não existe."}

    for attr, value in data.dict().items():
        setattr(personagem, attr, value)

    personagem.save()
    return 200, personagem

@api.delete("personagens/{personagem_id}/", response={204: None, 404: ErrorSchema}, tags=["Personagens"])
def delete_personagem(request, personagem_id: int):
    personagem = get_object_or_404(Personagem, id=personagem_id)
    personagem.delete()
    return 204, None



@api.get("missoes/", response={200: List[MissaoOut]}, tags=["Missões"])
def list_missoes(request):
    missoes = Missao.objects.select_related(
        "planeta_destino"
    ).prefetch_related(
        "participantes"
    ).all()

    return 200, missoes

@api.get("missoes/{missao_id}/", response={200: MissaoOut, 404: ErrorSchema}, tags=["Missões"])
def get_missao(request, missao_id: int):
    missao = get_object_or_404(
        Missao.objects.select_related("planeta_destino").prefetch_related("participantes"),
        id=missao_id
    )

    return 200, missao

@api.post("missoes/", response={201: MissaoOut, 400: ErrorSchema}, tags=["Missões"])
def post_missao(request, data: MissaoIn):
    if not Planeta.objects.filter(id=data.planeta_destino_id).exists():
        return 400, {"detail": "O planeta de destino indicado não existe."}

    dados = data.dict()
    participante_ids = dados.pop("participante_ids", [])

    if Personagem.objects.filter(id__in=participante_ids).count() != len(participante_ids):
        return 400, {"detail": "Uma ou mais personagens indicadas não existem."}

    missao = Missao.objects.create(**dados)
    missao.participantes.set(participante_ids)

    return 201, missao

@api.put("missoes/{missao_id}/", response={200: MissaoOut, 400: ErrorSchema, 404: ErrorSchema}, tags=["Missões"])
def put_missao(request, missao_id: int, data: MissaoIn):
    missao = get_object_or_404(Missao, id=missao_id)

    if not Planeta.objects.filter(id=data.planeta_destino_id).exists():
        return 400, {"detail": "O planeta de destino indicado não existe."}

    dados = data.dict()
    participante_ids = dados.pop("participante_ids", [])

    if Personagem.objects.filter(id__in=participante_ids).count() != len(participante_ids):
        return 400, {"detail": "Uma ou mais personagens indicadas não existem."}

    for attr, value in dados.items():
        setattr(missao, attr, value)

    missao.save()
    missao.participantes.set(participante_ids)

    return 200, missao

@api.delete("missoes/{missao_id}/", response={204: None, 404: ErrorSchema}, tags=["Missões"])
def delete_missao(request, missao_id: int):
    missao = get_object_or_404(Missao, id=missao_id)
    missao.delete()
    return 204, None
