from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Criar o filme
LISTA_CATEGORIAS = (
   #(nome no bd, nome da view)
    ("ANALISES", "Análises"),
    ("PROGRAMACAO","Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    views = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
    
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()
    
    
    def __str__(self):
        return self.titulo
    
# Classe para criar armazenar e gerenciar usuarios
class Usuario(AbstractUser):
    # Herda por padrão os atributos da classe abstract user, entao nesta classe irei colocar apenas campos novos a serem incluidos, campos como usuario, e senha nao serao definidos pois ja existem na classe pai e nao desejo sobrescreve-los.
    filmes_vistos = models.ManyToManyField('Filme')
