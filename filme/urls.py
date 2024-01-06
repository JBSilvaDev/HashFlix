from django.urls import path
from .views import *

# Nome passado no arquivo de url padrão no paramentro namespace (opcional) usado quando há urls com mesmo nome para diferenciar a que app pertence
app_name = "filme"

urlpatterns = [
    path("", HomePage.as_view(), name="homepage"),
    path("filmes/", HomeFilmes.as_view(), name="homeFilmes"),
    path("filmes/<int:pk>", DetalhesFilme.as_view(), name="detalhesFilme"),
    path("pesquisa/", PesquisaFilme.as_view(), name="pesquisaFilme"),
]
