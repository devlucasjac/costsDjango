from django.contrib import admin
from .models import Categoria,Serviço,Projeto
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome','criação','atualização','ativo')

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
     list_display = ('nome','criação','atualização','ativo','orçamento','categoria')  

@admin.register(Serviço)
class ServiçoAdmin(admin.ModelAdmin):
     list_display = ('nome','criação','atualização','ativo','custo','descrição','projeto')  

      