from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    
    path("", views.home, name="home"),
    path("licenciatura/", views.licenciatura, name="licenciatura"),
    path("projetos/", views.projetos, name="projetos"),
    path("tecnologias/", views.tecnologias, name="tecnologias"),
    path("tfc/", views.tfc, name="tfc"),
    path("makingof/", views.makingof, name="makingof"),
    path("competencias/", views.competencias, name="competencias"),
    path("formacao/", views.formacoes, name="formacoes"),
    path("uc/<int:uc_id>/", views.uc, name="ucs"),

    path("novo_projeto/", views.novo_projeto, name = "novo_projeto"),
    path("edita_projeto/<int:projeto_id>/", views.edita_projeto, name="edita_projeto"),
    path("apaga_projeto/<int:projeto_id>/", views.apaga_projeto, name="apaga_projeto"),

    path("tecnologias/nova/", views.nova_tecnologia, name="nova_tecnologia"),
    path("tecnologias/<int:tecnologia_id>/editar/", views.editar_tecnologia, name="editar_tecnologia"),
    path("tecnologias/<int:tecnologia_id>/apagar/", views.apagar_tecnologia, name="apagar_tecnologia"),

    path("competencias/nova/", views.nova_competencia, name="nova_competencia"),
    path("competencias/<int:competencia_id>/editar/", views.editar_competencia, name="editar_competencia"),
    path("competencias/<int:competencia_id>/apagar/", views.apagar_competencia, name="apagar_competencia"),

    path("formacoes/nova/", views.nova_formacao, name="nova_formacao"),
    path("formacoes/<int:formacao_id>/editar/", views.editar_formacao, name="editar_formacao"),
    path("formacoes/<int:formacao_id>/apagar/", views.apagar_formacao, name="apagar_formacao"),
]