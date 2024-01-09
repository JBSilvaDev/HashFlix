from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view
# Nome passado no arquivo de url padrão no paramentro namespace (opcional) usado quando há urls com mesmo nome para diferenciar a que app pertence
app_name = "filme"

urlpatterns = [
    path("", HomePage.as_view(), name="homepage"),
    path("filmes/", HomeFilmes.as_view(), name="homeFilmes"),
    path("filmes/<int:pk>", DetalhesFilme.as_view(), name="detalhesFilme"),
    path("pesquisa/", PesquisaFilme.as_view(), name="pesquisaFilme"),
    # Url para criar pagina de login usando a login view padrao do django
    path('login/', auth_view.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'logout.html'), name='logout') #https://docs.djangoproject.com/en/5.0/topics/auth/default/#how-to-log-a-user-out

]
