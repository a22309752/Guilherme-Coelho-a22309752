from ninja import Schema

class FaccaoIn(Schema):
    nome: str
    lado: str
    descricao: str
    
class FaccaoOut(FaccaoIn):
    id: int
    

class PlanetaIn(Schema):
    nome: str
    clima: str
    setor: str
    faccao_id: int

class PlanetaOut(PlanetaIn):
    id: int
    faccao: FaccaoOut 

class PersonagemIn(Schema):
    nome: str
    idade: int
    especie: str 
    primeira_aparicao: str
    planeta_origem_id: int
    faccao_id: int 

class PersonagemOut(PersonagemIn):
    id: int
    planeta_origem: PlanetaOut
    faccao: FaccaoOut 


class MissaoIn(Schema):
    titulo: str
    dificuldade: str
    objetivo: str
    planeta_destino_id: int
    participantes_id: int

class MissaoOut(MissaoIn):
    id: int
    planeta_destino: PlanetaOut
    participantes: PersonagemOut

class ErrorSchema(Schema):
    detail: str