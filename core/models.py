from django.db import models


class Setor(models.Model):
  codigo = models.CharField(max_length=10, primary_key=True)
  nome = models.CharField(max_length=100)
  caminho = models.CharField(max_length=100)
  unidade_sigla = models.CharField(max_length=10)
  unidade_nome = models.CharField(max_length=100)

  def __str__(self):
    return self.nome
