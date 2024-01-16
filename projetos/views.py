from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Categoria, Serviço, Projeto
from .serializers import CategoriaSerializer,ServiçoSerializer,ProjetoSerializer,ProjetoListSerializer
# Create your views here.


class CategoriaViewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ServiçoViewset(viewsets.ModelViewSet):
    queryset = Serviço.objects.all()
    serializer_class = ServiçoSerializer

class ProjetoViewset(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

    def retrieve(self, request, pk=None):
        queryset = Projeto.objects.all()
        projeto = get_object_or_404(queryset, pk=pk)
        serializer = ProjetoListSerializer(projeto)  
        serviços = Serviço.objects.filter(projeto_id=pk)
        custo = 0
        if serviços is not None:
            for serviço in serviços:
                custo += serviço.custo        

        retrieveProject ={
            "id": serializer.data['id'],
            "nome": serializer.data['nome'],
            "orçamento": serializer.data['orçamento'],
            "categoria":serializer.data['categoria'],
            "custo":custo
        }       
        return Response(retrieveProject)

    def list(self,request):
        queryset = Projeto.objects.all()
        serializers = ProjetoListSerializer(queryset,many=True)

        return Response(serializers.data)
    