from django.contrib import admin

# Register your models here.
from .models import Receita
admin.site.register(Receita)

from .models import Ingrediente
admin.site.register(Ingrediente)

from .models import Utilizador
admin.site.register(Utilizador)
