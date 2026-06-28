from django.urls import path
from . import views

urlpatterns = [
    path("api-colega/campeoes/", views.lista_campeoes_colega, name="lista_campeoes_colega"),
    path("api-colega/campeoes/novo/", views.criar_campeao_colega, name="criar_campeao_colega"),
    path("api-colega/campeoes/<int:campeao_id>/", views.detalhe_campeao_colega, name="detalhe_campeao_colega"),
    path("api-colega/campeoes/<int:campeao_id>/editar/", views.editar_campeao_colega, name="editar_campeao_colega"),
    path("api-colega/campeoes/<int:campeao_id>/apagar/", views.apagar_campeao_colega, name="apagar_campeao_colega"),
]