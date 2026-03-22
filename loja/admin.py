from django.contrib import admin

# Register your models here.
from .models import Loja
admin.site.register(Loja)

from .models import Categoria
admin.site.register(Categoria)

from .models import Produto
admin.site.register(Produto)

from .models import Cliente
admin.site.register(Cliente)

from .models import Morada
admin.site.register(Morada)

from .models import Pedido
admin.site.register(Pedido)

from .models import Item
admin.site.register(Item)