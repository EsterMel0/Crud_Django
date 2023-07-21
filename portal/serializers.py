from rest_framework import serializers
from portal.models import Autor, Editora, Livro


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class EditoraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'


class LivroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
