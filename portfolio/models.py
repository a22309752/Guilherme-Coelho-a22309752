from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    formato_curso = models.CharField(max_length=100,blank= True, null=True)
    duracao = models.CharField(max_length=100)
    semestres = models.IntegerField(blank= True, null=True)
    creditos = models.CharField(max_length=100,blank= True, null=True)
    descricao = models.TextField(blank= True, null=True)
    requisitos = models.JSONField(blank= True, null=True)
    url_oficial = models.URLField(blank= True, null=True)

    class Meta:
        verbose_name = "Licenciatura"
        verbose_name_plural = "Licenciaturas"
         
    def __str__(self):
        return self.nome


class Docente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    url_oficial = models.URLField(blank= True, null=True)

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"
    
    def __str__(self):
        return self.nome


class Unidade_Curricular(models.Model):
    nome = models.CharField(max_length=100)
    ano_curricular = models.IntegerField()
    semestre = models.IntegerField()
    url_oficial = models.URLField(blank= True, null=True)
    imagem = models.ImageField(upload_to="media/")
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name= "UCs",blank= True, null=True)
    docente = models.ManyToManyField(Docente, related_name= "UCs")
    
    class Meta:
        verbose_name = "Unicade Curricular"
        verbose_name_plural = "Unidades Curriculares"
    
    def __str__(self):
        return self.nome



class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    url_oficial = models.URLField(blank= True, null=True)
    logo_oficial = models.ImageField(upload_to= "media/")
    descricao = models.TextField(blank=True,null=True)
    nivel_interesse = models.IntegerField(validators=[MinValueValidator(0),
            MaxValueValidator(10)])
    
    class Meta:
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"
    
    def __str__(self):
        return self.nome


class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Competência"
        verbose_name_plural = "Competências"
    
    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    ano_curricular = models.IntegerField()
    semestre = models.IntegerField()
    descricao = models.TextField(blank=True,null=True)
    imagem = models.ImageField(upload_to="media/")
    conceitos_aplicados = models.CharField(max_length= 100)
    uc = models.ForeignKey(Unidade_Curricular, on_delete=models.CASCADE, related_name="projetos",blank= True, null=True)
    tecnologia = models.ManyToManyField(Tecnologia, related_name="projetos")
    competencia = models.ManyToManyField(Competencia, related_name="projetos")

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
    
    def __str__(self):
        return self.nome



class Formacao(models.Model):
    nome = models.CharField(max_length=100)
    url_oficial = models.URLField(blank= True, null=True)
    logo_oficial = models.ImageField(upload_to= "media/")
    descrição = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    
    class Meta:
        verbose_name = "Formacao"
        verbose_name_plural = "Formações"
    
    def __str__(self):
        return self.nome


class MakingOf(models.Model):
 
    entidades = [
        ("licenciatura", "Licenciatura"),
        ("unidade_curricular", "Unidade Curricular"),
        ("docente", "Docente"),
        ("projeto", "Projeto"),
        ("tecnologia", "Tecnologia"),
        ("competencia", "Competência"),
        ("formacao", "Formação"),
        ("tfc", "TFC"),  
    ]

    titulo = models.CharField(max_length=100)
    entidade = models.CharField(max_length=100,choices=entidades,default="nenhuma")
    descricao_trabalho = models.TextField()
    decisoes_tomadas = models.TextField()
    erros_encontrados = models.TextField(blank=True)
    correcoes_realizadas = models.TextField(blank=True)
    imagem1 = models.ImageField(upload_to="makingof/", blank=True, null=True)
    imagem2 = models.ImageField(upload_to="makingof/", blank=True, null=True)

    class Meta:
        verbose_name = "MakingOf"
        verbose_name_plural = "MakingOf"

    def __str__(self):
        return self.titulo

    
class TFC(models.Model):
    titulo = models.CharField(max_length=300)
    autor = models.CharField(max_length=300)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="media/")

    class Meta:
        verbose_name = "TFC"
        verbose_name_plural = "TFCs"

    def __str__(self):
        return self.titulo


    