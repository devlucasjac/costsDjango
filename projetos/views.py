from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Categoria, Serviço, Projeto
from .serializers import CategoriaSerializer,ServiçoSerializer,ProjetoSerializer,ProjetoListSerializer
# Create your views here.

def calculoCusto(lista): 
    custo=0
    if lista is not None:
       for item in lista:
           custo += item.custo  
    return custo

class CategoriaViewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ServiçoViewset(viewsets.ModelViewSet):
    queryset = Serviço.objects.all()
    serializer_class = ServiçoSerializer  

    def create(self,request):
        project_id = request.data["projeto"]
        queryset = Projeto.objects.all()
        projeto = get_object_or_404(queryset, pk=project_id)

        orçamento = projeto.orçamento

        serviços = Serviço.objects.filter(projeto_id=project_id)
        custo_total = calculoCusto(serviços) + float(request.data["custo"])

        serializer = ServiçoSerializer(data=request.data)
       
        if custo_total < orçamento and serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response("O custo total dos serviços não deve exceder o orçamento do projeto",status=status.HTTP_400_BAD_REQUEST)

class ProjetoViewset(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

    @action(detail=True,methods=["GET"])
    def serviços(self,request,pk=None):
        serviços = Serviço.objects.filter(projeto_id=pk)
        serializer = ServiçoSerializer(serviços,many="True")       
        return Response(serializer.data)

    def update(self,request,pk=None):
        queryset = Projeto.objects.all()
        projeto = get_object_or_404(queryset, pk=pk)        
        serializer = ProjetoSerializer(projeto,data=request.data)  

        serviços = Serviço.objects.filter(projeto_id=pk)
        custo = calculoCusto(serviços)        

        orçamento = float(request.data["orçamento"])

        if custo < orçamento:                   
            if serializer.is_valid():                
                serializer.save()
                return Response(serializer.data)   
                         
        return Response("Não é possivel criar um projeto com um orçamento menor que o custo",status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Projeto.objects.all()
        projeto = get_object_or_404(queryset, pk=pk)
        serializer = ProjetoListSerializer(projeto) 

        serviços = Serviço.objects.filter(projeto_id=pk)
       
        custo=calculoCusto(serviços)

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
    