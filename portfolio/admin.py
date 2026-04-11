from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Licenciatura)
admin.site.register(Unidade_Curricular)
admin.site.register(Docente)
admin.site.register(Projeto)
admin.site.register(Tecnologia)
admin.site.register(Competencia)
admin.site.register(Formacao)
admin.site.register(MakingOf)
