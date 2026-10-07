from django.urls import path

from . import views

app_name = "estoque"

urlpatterns = [
    path(
        "categorias/",
        views.categoria_lista,
        name="categoria_lista",
    ),

    path(
        "categorias/nova/",
        views.categoria_criar,
        name="categoria_criar",
    ),

    path(
        "categorias/<int:pk>/editar/",
        views.categoria_editar,
        name="categoria_editar",
    ),

    path(
        "categorias/<int:pk>/excluir/",
        views.categoria_excluir,
        name="categoria_excluir",
    ),
    path(
            "fornecedores/",
            views.FornecedorListView.as_view(),
            name="fornecedores_lista",
        ),

        path(
            "fornecedores/novo/",
            views.FornecedorCreateView.as_view(),
            name="fornecedor_novo",
        ),

        path(
            "fornecedores/<int:pk>/editar/",
            views.FornecedorUpdateView.as_view(),
            name="fornecedor_editar",
        ),

        path(
            "fornecedores/<int:pk>/excluir/",
            views.FornecedorDeleteView.as_view(),
            name="fornecedor_excluir",
        ),
]