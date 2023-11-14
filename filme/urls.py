from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePage.as_view()),
    path("filmes/", HomeFilmes.as_view()),
    path("filmes/<int:id>", DetalhesFilme.as_view()),
]