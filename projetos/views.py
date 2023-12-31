from rest_framework.response import Response
from rest_framework import viewsets, mixins
from .models import Categoria, Serviço, Projeto
from .serializers import CategoriaSerializer,ServiçoSerializer,ProjetoSerializer
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