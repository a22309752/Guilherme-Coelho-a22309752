from django.contrib import admin

# Register your models here.
from .models import Escola
admin.site.register(Escola)

from .models import Turma
admin.site.register(Turma)

from .models import Aluno
admin.site.register(Aluno)

from .models import Professor
admin.site.register(Professor)