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
]
