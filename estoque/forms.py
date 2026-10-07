from django import forms

from .models import Categoria, Fornecedor, Produto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome", "descricao", "ativo"]


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = [
            "nome",
            "email",
            "telefone",
            "ativo",
        ]

        labels = {
            "nome": "Nome",
            "email": "E-mail",
            "telefone": "Telefone",
            "ativo": "Ativo",
        }

        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "placeholder": "Digite o nome do fornecedor",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Digite o e-mail",
                }
            ),
            "telefone": forms.TextInput(
                attrs={
                    "placeholder": "Digite o telefone",
                }
            ),
        }


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