from django.urls import path
from .views import artigo_view, like_view, comentar_view, editar_artigo_view
app_name = "artigos"

urlpatterns = [
    path("", artigo_view, name="artigo"),
    path("like/", like_view, name= "like"),
    path("comentar/", comentar_view, name="comentar"),
    path("editar/<int:artigo_id>/", editar_artigo_view, name="editar"),
]