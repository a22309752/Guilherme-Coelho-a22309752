from django.db import models

# Create your models here.

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    duracao = models.CharField(max_length=100)
    url_pagina_oficial = models.URLField()
    requisitos = models.TextField()

    class Meta:
        verbose_name = "Licenciatura"
        verbose_name_plural = "Licenciaturas"

    def __str__(self):
        return self.nome


class Docente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    pagina_pessoal_url = models.URLField()

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"

    def __str__(self):
        return self.nome


class Unidade_Curricular(models.Model):
    nome = models.CharField(max_length=200)
    ano_curricular = models.IntegerField()
    semestre = models.IntegerField()
    url_uc = models.URLField()
    imagem_url = models.URLField()
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name= "UCs")
    docente = models.ManyToManyField(Docente, related_name= "UCs")

    class Meta:
        verbose_name = "Unidade Curricular"
        verbose_name_plural = "Unidades Curriculares"

    def __str__(self):
        return self.nome


class Competencia(models.Model):
    nome = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Competência"
        verbose_name_plural = "Competências"

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    nome =  models.CharField(max_length=100)
    url_oficial = models.URLField()
    descricao = models.TextField()
    logo_url = models.URLField()
    nivel_interesse = models.IntegerField()
    nivel_proficiencia = models.IntegerField()
    
    class Meta:
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem_url = models.URLField()
    link_projeto = models.URLField()
    ano_curricular = models.IntegerField()
    uc = models.ForeignKey(Unidade_Curricular, on_delete=models.CASCADE, related_name="projetos")
    tecnologia = models.ManyToManyField(Tecnologia, related_name="projetos")
    competencia = models.ManyToManyField(Competencia, related_name="projetos")

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()

    class Meta:
        verbose_name = "Formação"
        verbose_name_plural = "Formações"

    def __str__(self):
        return self.nome


class MakingOf(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem_url = models.URLField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Making Of"
        verbose_name_plural = "Making Of"

    def __str__(self):
        return self.titulo


class TFC(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    resumo = models.TextField()
    imagem = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "TFC"
        verbose_name_plural = "TFCs"

    def __str__(self):
        return self.titulo