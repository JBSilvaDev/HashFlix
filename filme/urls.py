from django.urls import path
from .views import *

app_name = 'filme'

urlpatterns = [
    path("", HomePage.as_view(), name='homepage'),
    path("filmes/", HomeFilmes.as_view(), name='homeFilmes'),
    path("filmes/<int:pk>", DetalhesFilme.as_view(), name='datalhesFilme'),
]