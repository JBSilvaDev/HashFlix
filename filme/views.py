# from django.shortcuts import render
from typing import Any
from filme.models import Filme
from django.views.generic import TemplateView, ListView, DetailView


# def homepage(request):
#    return render(request, 'homepage.html')
class HomePage(TemplateView):
    # Nome do arquivo HTML
    template_name = "homepage.html"


# def homeFilmes(request):
#    lista_filmes = Filme.objects.all()
#    return render(request, 'homeFilmes.html', {"lista":lista_filmes})
class HomeFilmes(ListView):
    # Nome do arquivo HTML
    template_name = "homeFilmes.html"
    # Modelo que sera listado no HTML ( passa como nome object_list que contem todos itens do modelo )
    model = Filme


# Por padrão esta classe espera um paramentro na url
class DetalhesFilme(DetailView):
    # Nome do arquivo HTML
    template_name = "detalhesFilme.html"
    # Modelo que sera listado no HTML ( passa como nome object que contem 1 item do nosso modelo )
    model = Filme

    def get_context_data(self, **kwargs):
        context = super(DetalhesFilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados']=filmes_relacionados
        return context
