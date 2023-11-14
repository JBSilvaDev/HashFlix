from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePage.as_view()),
    path("filmes/", HomeFilmes.as_view()),
    path("filmes/<int:pk>", DetalhesFilme.as_view()),
]