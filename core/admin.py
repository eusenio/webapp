from django.contrib import admin
from django.contrib.admin.decorators import display

from .models import (Endereco, Cliente)


admin.site.site_header = 'CRM Administração'

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['cidade','bairro','logradouro','uf']
    search_fields = ['cidade']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome','cpf','fone','email','data_cadastro']
    search_fields = ['nome']

