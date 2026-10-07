from django import forms

from .models import Categoria, Fornecedor, Produto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome", "descricao", "ativo"]


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ["nome", "email", "telefone", "ativo"]


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            "nome",
            "sku",
            "descricao",
            "preco_compra",
            "preco_venda",
            "quantidade_estoque",
            "estoque_minimo",
            "categoria",
            "fornecedor",
            "ativo",
        ]