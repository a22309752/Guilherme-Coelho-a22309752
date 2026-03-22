from django.db import models

# Create your models here.

class Utilizador(models.Model):
    nome = models.CharField(max_length=100)

def _str_(self):
    return self.nome


class Receita(models.Model):
    nome = models.CharField(max_length=100)
    utilizador = models.ManyToManyField(Utilizador, related_name='receitas_favoritas') #utilizador N:M receita
    

def _str_(self):
    return self.nome

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    receita= models.ManyToManyField(Receita, related_name="ingredientes") #receita N:M ingrediente


def _str_(self):
    return self.nome

