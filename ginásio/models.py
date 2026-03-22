from django.db import models

# Create your models here.
class Ginásio(models.Model):
    nome= models.CharField(max_length =100)

def _str_(self):
    return self.nome

class PTs(models.Model):
    nome= models.CharField(max_length =100)
    ginasio = models.ForeignKey(Ginásio,on_delete= models.CASCADE, related_name= "pts") #ginásio 1:N pts

def _str_(self):
    return self.nome


class Membro(models.Model):
    nome= models.CharField(max_length =100)

def _str_(self):  
    return self.nome

class Sessão(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    membro = models.ForeignKey(Membro, on_delete= models.CASCADE, related_name= "sessões") #membro 1:N sessão
    pt = models.ForeignKey(PTs, on_delete = models.CASCADE, related_name= "sessões") #pt 1:N sessão

    class Meta:
        unique_together = ('pt', 'data', 'hora')
    
def _str_(self):
    return f'{self.data}: {self.hora} '

  