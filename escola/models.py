from django.db import models

# Create your models here.
class Escola(models.Model):
    nome= models.CharField(max_length =100)

def _str_(self):
    return self.nome

class Professor (models.Model):
    nome = models.CharField(max_length =100)
    email = models.EmailField()
    escola = models.ForeignKey(Escola, on_delete = models.CASCADE, related_name="professores",null=True, blank=True ) #escola 1:N professor

def _str_(self):
    return f'{self.nome}: {self.email}'


class Turma (models.Model):
    letra = models.CharField(max_length= 10)
    escola = models.ForeignKey(Escola, on_delete = models.CASCADE, related_name="turmas",null=True, blank=True ) #escola 1:N turma
    professor = models.OneToOneField(Professor, on_delete=models.CASCADE, related_name="turma") #professor 1:1 turma


def _str_(self):
    return self.letra

class Aluno (models.Model):
    nome = models.CharField(max_length =100)
    numero_aluno = models.IntegerField()
    escola = models.ForeignKey(Escola, on_delete = models.CASCADE, related_name="alunos" ) #escola 1:N aluno
    turma = models.ForeignKey(Turma, on_delete = models.CASCADE, related_name= "alunos") #turma 1:N aluno

def _str_(self):
    return f'{self.nome}: {self.numero_aluno} '

