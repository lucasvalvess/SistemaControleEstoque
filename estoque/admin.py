from django.contrib import admin

from .models import Categoria, Fornecedor, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "ativo", "criado_em")
    search_fields = ("nome",)
    list_filter = ("ativo",)


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone", "ativo")
    search_fields = ("nome", "email")
    list_filter = ("ativo",)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "sku",
        "categoria",
        "fornecedor",
        "quantidade_estoque",
        "estoque_minimo",
        "preco_venda",
        "ativo",
    )

    search_fields = ("nome", "sku")
    list_filter = ("categoria", "fornecedor", "ativo")
    list_select_related = ("categoria", "fornecedor")

    @admin.display(boolean=True, description="Estoque baixo")
    def estoque_baixo(self, obj):
        return obj.estoque_baixo