from django.db import models

# Create your models here.

class Loja(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    loja = models.ForeignKey(Loja, on_delete= models.CASCADE, related_name= "produtos",null=True, blank=True) #loja 1:N produto
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE, related_name= "produtos",null=True, blank=True) #categoria 1:N produto

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Morada(models.Model):
    rua = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)
    cliente = models.OneToOneField(Cliente, on_delete= models.CASCADE, related_name="morada",null=True, blank=True) #cliente 1:N pedido

    def __str__(self):
        return f"{self.rua}, {self.cidade}"


class Pedido(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pedidos",null=True, blank=True) #cliente 1:N pedido

    def __str__(self):
        return f"Pedido {self.id}"


class Item(models.Model):
    quantidade = models.IntegerField()
    produto = models.ForeignKey(Produto, on_delete= models.CASCADE, related_name="items",null=True, blank=True) #produto 1:N item
    pedido = models.ForeignKey(Pedido, on_delete= models.CASCADE, related_name="items",null=True, blank=True) #pedido 1:N item

    def __str__(self):
        return f"Quantidade: {self.quantidade}"