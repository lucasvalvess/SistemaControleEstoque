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
        
        labels = {
            "nome": "Nome",
            "sku": "SKU",
            "descricao": "Descrição",
            "preco_compra": "Preço de compra",
            "preco_venda": "Preço de venda",
            "quantidade_estoque": "Quantidade em estoque",
            "estoque_minimo": "Estoque mínimo",
            "categoria": "Categoria",
            "fornecedor": "Fornecedor",
            "ativo": "Ativo",
        }

        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "placeholder": "Digite o nome do produto",
                }
            ),

            "sku": forms.TextInput(
                attrs={
                    "placeholder": "Ex: MOU-001",
                }
            ),

            "descricao": forms.Textarea(
                attrs={
                    "placeholder": "Digite uma descrição do produto",
                    "rows": 4,
                }
            ),

            "preco_compra": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "min": "0",
                    "placeholder": "0,00",
                }
            ),

            "preco_venda": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "min": "0",
                    "placeholder": "0,00",
                }
            ),

            "quantidade_estoque": forms.NumberInput(
                attrs={
                    "min": "0",
                }
            ),

            "estoque_minimo": forms.NumberInput(
                attrs={
                    "min": "0",
                }
            ),

            "categoria": forms.Select(),

            "fornecedor": forms.Select(),
        }