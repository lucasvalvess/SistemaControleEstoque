from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoriaForm
from .models import Categoria


from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.deletion import ProtectedError
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import FornecedorForm
from .models import Fornecedor


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


class FornecedorListView(ListView):
    model = Fornecedor
    template_name = "estoque/fornecedores/lista.html"
    context_object_name = "fornecedores"


class FornecedorCreateView(SuccessMessageMixin, CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = "estoque/fornecedores/form.html"
    success_url = reverse_lazy("estoque:fornecedores_lista")
    success_message = "Fornecedor criado com sucesso."


class FornecedorUpdateView(SuccessMessageMixin, UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = "estoque/fornecedores/form.html"
    success_url = reverse_lazy("estoque:fornecedores_lista")
    success_message = "Fornecedor atualizado com sucesso."


class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    template_name = "estoque/fornecedores/confirmar_exclusao.html"
    success_url = reverse_lazy("estoque:fornecedores_lista")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        try:
            self.object.delete()
        except ProtectedError:
            messages.error(
                request,
                "Não é possível excluir este fornecedor porque existem produtos vinculados a ele."
            )
        else:
            messages.success(
                request,
                "Fornecedor excluído com sucesso."
            )

        return redirect(self.success_url)