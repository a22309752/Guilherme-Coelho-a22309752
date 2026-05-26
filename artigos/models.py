from django.db import models
from django.contrib.auth.models import User

class Artigo(models.Model):
    titulo = models.CharField(max_length = 100)
    texto = models.TextField()
    fotografia = models.ImageField(upload_to = "media/")
    link_externo = models.URLField(blank = True, null = True)
    data_de_criação = models.DateField(auto_now_add = True)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)

    likes = models.ManyToManyField(
        User,
        related_name="artigos_liked",
        blank=True
    )

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    texto = models.TextField()
    criado_em = models.DateField(auto_now_add = True)
    artigo = models.ForeignKey(Artigo, on_delete = models.CASCADE, related_name = "comentarios")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto

LIKE_CHOICES = (
    ("Like", "Like"),
    ("Unlike", "Unlike"),
)
class Like(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    value = models.CharField(choices = LIKE_CHOICES, default = "like", max_length = 10)

    class Meta:
        unique_together = ("autor", "artigo")

    def __str__(self):
        return str(self.value)


