# from django.shortcuts import render
from typing import Any
from filme.models import Filme
from django.views.generic import TemplateView, ListView, DetailView


# def homepage(request):
#    return render(request, 'homepage.html')
class HomePage(TemplateView):
    template_name = "homepage.html"


# def homeFilmes(request):
#    lista_filmes = Filme.objects.all()
#    return render(request, 'homeFilmes.html', {"lista":lista_filmes})


class HomeFilmes(ListView):
    # object_list -> lista de itens do modelo
    template_name = "homeFilmes.html"
    model = Filme


class DetalhesFilme(DetailView):
    # object -> 1 item do nosso modelo
    template_name = "detalhesFilme.html"
    model = Filme

    def get_context_data(self, **kwargs):
        context = super(DetalhesFilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados']=filmes_relacionados
        return context
