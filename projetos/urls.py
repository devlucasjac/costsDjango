from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProjetoViewset,CategoriaViewset,ServiçoViewset

router = SimpleRouter()
router.register('projetos',ProjetoViewset)
router.register('serviço',ServiçoViewset)
router.register('categoria',CategoriaViewset)
