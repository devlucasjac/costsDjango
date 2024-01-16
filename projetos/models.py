from django.db import models

# Create your models here.
class Base(models.Model):
    criação = models.DateTimeField(auto_now_add=True)
    atualização = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class  Categoria(Base):
    nome = models.CharField(max_length=255)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nome
  
class Projeto(Base):
    nome = models.CharField(max_length=255)
    orçamento = models.FloatField()
    categoria = models.ForeignKey(Categoria,related_name="projetos",on_delete=models.CASCADE)    

    class Meta:
        verbose_name = "projeto"
        verbose_name_plural = "projetos"
    
    def __str__(self):
        return f'o projeto {self.nome} tem o orçamento de {self.orçamento} e pertence a categoria {self.categoria}'


class Serviço(Base):
    nome = models.CharField(max_length=255)
    custo = models.FloatField()
    descrição = models.TextField(blank=True, default="")
    projeto = models.ForeignKey(Projeto,related_name="serviços",on_delete=models.CASCADE,blank=True,default=0)

    class Meta:
        verbose_name = "serviço"
        verbose_name_plural = "serviços"
    def __str__(self):
        return f'{self.nome} tem o custo de {self.custo} e se trata de{self.descrição}' 

    