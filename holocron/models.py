from django.db import models


class Faccao(models.Model):
    nome = models.CharField(max_length=100)
    lado = models.CharField(max_length=100)
    descricao = models.TextField()
    

    def __str__(self):
        return self.nome

class Planeta(models.Model):
    nome = models.CharField(max_length=100)
    clima = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    faccao = models.ForeignKey(
        Faccao,
        on_delete= models.SET_NULL,
        null= True,
        blank= True,
        related_name= "planetas",
    )

    def __str__(self):
        return self.nome


class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    especie = models.CharField(max_length=300)
    primeira_aparicao = models.TextField()

    planeta_origem = models.ForeignKey(
        Planeta, 
        on_delete= models.CASCADE,
        related_name= "personagens"
    )

    faccao = models.ForeignKey(
        Faccao,
        on_delete=models.CASCADE,
        related_name="personagens"
)

    def __str__(self):
        return self.nome

class Missao(models.Model):
    titulo = models.CharField(max_length=100)
    dificuldade = models.CharField(max_length=300)
    objetivo = models.TextField()

    planeta_destino = models.ForeignKey(
        Planeta,
        on_delete=models.CASCADE,
        related_name="missoes"
    )

    participantes = models.ForeignKey(
        Personagem,
        on_delete=models.CASCADE,
        related_name="missoes",
    )

    def __str__(self):
        return self.titulo


