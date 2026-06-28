
from django.contrib import admin
from .models import Planeta, Faccao, Personagem, Missao

admin.site.register(Planeta)
admin.site.register(Personagem)
admin.site.register(Faccao)
admin.site.register(Missao)