# Generated by Django 3.2.9 on 2021-11-20 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('logradouro', models.CharField(max_length=100)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AM', 'Amazonas'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('PA', 'Belem')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=18)),
                ('rg', models.CharField(max_length=14)),
                ('numero', models.CharField(max_length=6)),
                ('cep', models.CharField(max_length=14)),
                ('fone', models.CharField(max_length=11)),
                ('ativo', models.CharField(choices=[('A', 'Ativo'), ('I', 'Inativo')], max_length=1)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.endereco')),
            ],
        ),
    ]
