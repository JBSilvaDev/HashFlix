# from django.shortcuts import render
from typing import Any
# Importe para passar as views que exigem login para serem exibidas
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from filme.models import Filme
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from .forms import CreateAccountForm, EditProfileForm
from .models import Usuario
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
import re

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

        # Get the first episode and extract YouTube embed URL
        first_episode = self.get_object().episodios.first()
        if first_episode and first_episode.video:
            video_url = first_episode.video
            # Regex to extract YouTube video ID from various YouTube URL formats
            youtube_id_match = re.search(r'(?:https?://)?(?:www\.)?(?:youtube\.com|youtu\.be)/(?:watch\?v=|embed/|v/|)([a-zA-Z0-9_-]{11})', video_url)
            if youtube_id_match:
                youtube_video_id = youtube_id_match.group(1)
                embed_url = f"https://www.youtube.com/embed/{youtube_video_id}"
                context["embed_url"] = embed_url
            else:
                # Fallback or handle non-YouTube URLs if necessary
                context["embed_url"] = video_url # Use original URL if not YouTube, might not embed properly
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


class CriarConta(FormView):
    template_name = "criarconta.html"
    form_class = CreateAccountForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('filme:login')

    

    

class EditarPerfil(LoginRequiredMixin, UpdateView):

        template_name = "editarperfil.html"

        form_class = EditProfileForm

        model = Usuario

        def get_object(self):

            return self.request.user

        def get_success_url(self):

            return reverse_lazy('filme:homeFilmes')

    
def check_user_email(request):
    email_input = request.GET.get('email')
    if email_input:
        user_exists = Usuario.objects.filter(email__iexact=email_input).exists()
        if user_exists:
            return redirect(reverse_lazy('filme:login') )
        else:
            return redirect(reverse_lazy('filme:criarconta'))
    return redirect(reverse_lazy('filme:homepage'))