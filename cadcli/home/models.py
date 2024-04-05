from django.db import models

# Create your models here.
class Cliente(models.Model):
  nome = models.CharField(max_length=100)
  dtnasc = models.CharField(max_length=20)
  email = models.CharField(max_length=100)
  telefone = models.CharField(max_length=20)
  estado = models.CharField(max_length=5)
  genero = models.CharField(max_length=5)


  def __str__(self):
     return self.nome
