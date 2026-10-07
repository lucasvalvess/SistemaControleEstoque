from django.core.validators import MinValueValidator
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    ativo = models.BooleanField(default=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    sku = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True)

    preco_compra = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    preco_venda = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    quantidade_estoque = models.PositiveIntegerField(default=0)
    estoque_minimo = models.PositiveIntegerField(default=0)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="produtos"
    )

    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.PROTECT,
        related_name="produtos"
    )

    ativo = models.BooleanField(default=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome
    
    # Aqui, nós temos uma pequena regra do nosso domínio
    @property 
    def estoque_baixo(self):
        return self.quantidade_estoque <= self.estoque_minimo