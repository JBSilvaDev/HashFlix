# from django.shortcuts import render
from typing import Any
# Importe para passar as views que exigem login para serem exibidas
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from filme.models import Filme
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import logout


# def homepage(request):
#    return render(request, 'homepage.html')
class HomePage(TemplateView):
    # Nome do arquivo HTML
    template_name = "homepage.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homeFilmes')
        return super().get(request, *args, **kwargs) # retorna para o template name (url final)


# def homeFilmes(request):
#    lista_filmes = Filme.objects.all()
#    return render(request, 'homeFilmes.html', {"lista":lista_filmes})
class HomeFilmes(LoginRequiredMixin, ListView):
    # Nome do arquivo HTML
    template_name = "homeFilmes.html"
    # Modelo que sera listado no HTML ( passa como nome object_list que contem todos itens do modelo )
    model = Filme


# Por padrão esta classe espera um paramentro do item a ser detalhado, no caso o id do filme passado na url
class DetalhesFilme(LoginRequiredMixin, DetailView):
    # Nome do arquivo HTML
    template_name = "detalhesFilme.html"
    # Modelo que sera listado no HTML ( passa como nome object que contem 1 item do nosso modelo )
    model = Filme

    # Função padrão do django class base views que configura o context
    def get_context_data(self, **kwargs):
        # Executa o context original da classe, garantindo seu funcionamento
        context = super(DetalhesFilme, self).get_context_data(**kwargs)
        # Busca nos filmes categorias compativeis com o filme selecionado (object) self.get_objetc() tras os dados com objetc atual, no exemplo dados de categoria
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[ 0:5]  # Exibe no maxio 5 filmes com categorias iguais
        # Adiciona nova chave/valor ao dict context, passando os a variavel filmes_relacionados para o html
        context["filmes_relacionados"] = filmes_relacionados
        return context
    
    # Função padrão do django class base views que ira obter uma pagina
    def get(self, request, *args, **kwargs):
        # Descobrir pagina/objeto acessado
        filme = self.get_object()
        # Somanda +1 nas visualização do filme
        filme.views += 1
        # Salvando valor no db
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super(DetalhesFilme, self).get(request, *args, **kwargs) # Redireciona  usuario para o url final

# Classe que ira listar os filmes que correspontem a pesquisa
class PesquisaFilme(LoginRequiredMixin, ListView):
    # Nome do arquivo HTML
    template_name = "pesquisaFilme.html"
    # Modelo que sera listado no HTML ( passa como nome object que contem 1 item do nosso modelo )
    model = Filme

    # Função de pesquisa
    def get_queryset(self):
        # Obtem o que foi digitado no campo de nome pesquisa dentro do form
        termo_pesquisa = self.request.GET.get('pesquisa')
        if termo_pesquisa:
            object_list = Filme.objects.filter(titulo__icontains = termo_pesquisa)
            return object_list
        else:
            return None

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')