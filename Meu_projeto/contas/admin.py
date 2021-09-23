# Register your models here.

from django.contrib import admin
from .models import categorias
from .models import transacao


admin.site.register(categorias)
admin.site.register(transacao)


# maneira de testar o funcionamento do banco de dados

