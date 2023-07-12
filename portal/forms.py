from django import forms
from portal.models import Autor, Editora, Livro


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        exclude = ()  # lista todos os atributos

        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control', 'autofocus': ''}
            ),
            'data_nascimento': forms.DateInput(
                attrs={'class': 'form-control'}
            ),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }


class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        exclude = ()  # lista todos os atributos

        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control', 'autofocus': ''}
            ),
            'cidade': forms.TextInput(
                attrs={'class': 'form-control', 'autofocus': ''}
            ),
            'estado': forms.TextInput(
                attrs={'class': 'form-control', 'autofocus': ''}
            ),
        }


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        exclude = ()

        widgets = {
            'titulo': forms.TextInput(
                attrs={'class': 'form-control', 'autofocus': ''}
            )
        }
