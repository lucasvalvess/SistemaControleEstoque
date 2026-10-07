from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoriaForm
from .models import Categoria


def categoria_lista(request):
    categorias = Categoria.objects.all()

    contexto = {
        "categorias": categorias,
    }

    return render(
        request,
        "estoque/categorias/lista.html",
        contexto,
    )


def categoria_criar(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Categoria criada com sucesso."
            )

            return redirect("categoria_lista")

    else:
        form = CategoriaForm()

    contexto = {
        "form": form,
        "titulo": "Nova Categoria",
        "botao": "Cadastrar",
    }

    return render(
        request,
        "estoque/categorias/form.html",
        contexto,
    )


def categoria_editar(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == "POST":
        form = CategoriaForm(
            request.POST,
            instance=categoria,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Categoria atualizada com sucesso."
            )

            return redirect("categoria_lista")

    else:
        form = CategoriaForm(instance=categoria)

    contexto = {
        "form": form,
        "titulo": "Editar Categoria",
        "botao": "Salvar alterações",
    }

    return render(
        request,
        "estoque/categorias/form.html",
        contexto,
    )


def categoria_excluir(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == "POST":
        categoria.delete()

        messages.success(
            request,
            "Categoria excluída com sucesso."
        )

        return redirect("categoria_lista")

    contexto = {
        "categoria": categoria,
    }

    return render(
        request,
        "estoque/categorias/confirmar_exclusao.html",
        contexto,
    )