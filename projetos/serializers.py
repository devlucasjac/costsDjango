from rest_framework import serializers
from .models import Categoria,Serviço,Projeto

class CategoriaSerializer(serializers.ModelSerializer):
    #projetos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Categoria
        fields = [
            "id",
            "nome"
        ]

class ServiçoSerializer(serializers.ModelSerializer):
    #projetos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Serviço
        fields = [
            "id",
            "nome",
            "custo",
            "descrição"
        ]

class ProjetoSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Projeto
        fields = [
            "id",
            "nome",
            "orçamento",
            "categoria",
            "serviço"
        ]