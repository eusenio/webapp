from datetime import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

UF_CHOICES = (
    ('AC', 'Acre'),
    ('AM', 'Amazonas'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('PA', 'Belem')
)

STATUS_CHOICES = (
    ('A','Ativo'),
    ('I', 'Inativo')
)

class Endereco(models.Model):
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=100)
    uf = models.CharField(max_length=2, choices=UF_CHOICES)

    def __str__(self):
        return self.cidade

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=18)
    rg = models.CharField(max_length=14)
    endereco = models.ForeignKey(Endereco,on_delete=models.RESTRICT)
    numero = models.CharField(max_length=6)
    cep = models.CharField(max_length=14)
    fone = models.CharField(max_length=11)
    email = models.EmailField('E-mail',null=True,blank=True)
    ativo = models.CharField(max_length=1, choices=STATUS_CHOICES)
    data_cadastro = models.DateTimeField( default=datetime.now(),null=True, blank=True)

    def dtacadastro(self):
        self.data_cadastro = timezone.now()
        self.save()

    def __str__(self):
        return self.nome
