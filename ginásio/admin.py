from django.contrib import admin

# Register your models here.
from .models import Ginásio
admin.site.register(Ginásio)

from .models import PTs
admin.site.register(PTs)

from .models import Membro
admin.site.register(Membro)

from .models import Sessão
admin.site.register(Sessão)