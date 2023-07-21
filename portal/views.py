# flake8:noqa

from django.shortcuts import redirect, render
from portal.forms import AutorForm, EditoraForm, LivroForm
from portal.models import Autor, Editora, Livro
from rest_framework import viewsets
from portal.serializers import AutorSerializer, EditoraSerializer, LivroSerializer


# Create your views here.
def home(request):
    return render(request, 'portal/home.html')


def dashboard(request):
    return render(request, 'portal/dashboard.html')




def autor(request):
    autores = Autor.objects.all()
    context = {
        'autores': autores
    }
    return render(request, 'portal/autor.html', context)


def autor_add(request):
    form = AutorForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('autor')

    context = {
        'form': form
    }

    return render(request, 'portal/autor-add.html', context)


def autor_edit(request, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)

    form = AutorForm(request.POST or None, instance=autor)

    if request.POST:
        if form.is_valid():
           form.save()
           return redirect('autor')

    context = {
        'form': form,
    }

    return render(request, 'portal/autor-edit.html', context)


def autor_delete(request, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)

    autor.delete()

    return redirect('autor')






def editora(request):
    editoras = Editora.objects.all()
    context = {
        'editoras': editoras
    }
    return render(request, 'portal/editora.html', context)


def editora_add(request):
    form = EditoraForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('editora')

    context = {
        'form': form
    }

    return render(request, 'portal/editora-add.html', context)



def editora_edit(request, editora_pk):
    editora = Editora.objects.get(pk=editora_pk)

    form = EditoraForm(request.POST or None, instance=editora)

    if request.POST:
        if form.is_valid():
           form.save()
           return redirect('editora')

    context = {
        'form': form,
    }

    return render(request, 'portal/editora-edit.html', context)


def editora_delete(request, editora_pk):
    editora = Editora.objects.get(pk=editora_pk)

    editora.delete()

    return redirect('editora')









def livro(request):
    livro = Livro.objects.all()

    context = {
        'livro': livro
    }
    return render(request, 'portal/livro.html', context)


def livro_add(request):
    form = LivroForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('livros')

    context = {
        'form': form
    }

    return render(request, 'portal/livro-add.html', context)


def livro_edit(request, livro_pk):
    livro = Livro.objects.get(pk=livro_pk)

    form = LivroForm(request.POST or None, instance=livro)

    if request.POST:
        if form.is_valid():
           form.save()
           return redirect('livros')

    context = {
        'form': form,
    }

    return render(request, 'portal/livro-edit.html', context)


def livro_delete(request, livro_pk):
    livro = Livro.objects.get(pk=livro_pk)

    livro.delete()

    return redirect('livros')




def formato(request):
    return render(request, 'portal/formato.html')
