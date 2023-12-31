# flake8:noqa

"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from portal import views


urlpatterns = [
    path('', views.home, name="home"),
    
    path('autor/', views.autor, name="autor"),
    path('autor/add/', views.autor_add, name="autor_add"),
    path('autor/edit/<int:autor_pk>/', views.autor_edit, name="autor_edit"),
    path('autor/delete/<int:autor_pk>/', views.autor_delete, name="autor_delete"),

    path('editora/', views.editora, name="editora"),
    path('editora/add/', views.editora_add, name="editora_add"),
    path('editora/edit/<int:editora_pk>/', views.editora_edit, name="editora_edit"),
    path('editora/delete/<int:editora_pk>/', views.editora_delete, name="editora_delete"),

    path('livros/', views.livro, name="livros"),
    path('livros/add/', views.livro_add, name="livro_add"),
    path('livros/edit/<int:livro_pk>/', views.livro_edit, name="livro_edit"),
    path('livros/delete/<int:livro_pk>', views.livro_delete, name="livro_delete"),
]
