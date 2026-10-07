from django.urls import path

from . import views


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
]