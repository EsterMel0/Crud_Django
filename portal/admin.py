# flake8: noqa
from django.contrib import admin
from .models import Autor, Editora, Livro, Formato


class AutorAdmin(admin.ModelAdmin):
    ...


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    ...


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    ...


@admin.register(Formato)
class FormatoAdmin(admin.ModelAdmin):
    ...


admin.site.register(Autor, AutorAdmin)
