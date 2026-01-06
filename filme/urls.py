from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view
from .forms import LoginForm # Importar LoginForm

# Nome passado no arquivo de url padrão no paramentro namespace (opcional) usado quando há urls com mesmo nome para diferenciar a que app pertence
app_name = "filme"

urlpatterns = [
    path("", HomePage.as_view(), name="homepage"),
    path("filmes/", HomeFilmes.as_view(), name="homeFilmes"),
    path("filmes/<int:pk>", DetalhesFilme.as_view(), name="detalhesFilme"),
    path("pesquisa/", PesquisaFilme.as_view(), name="pesquisaFilme"),
    # Url para criar pagina de login usando a login view padrao do django
    path('login/', auth_view.LoginView.as_view(template_name = 'login.html', authentication_form=LoginForm), name='login'), # Usar LoginForm
    path('logout/', logout_view, name='logout'),
    path('criarconta/', CriarConta.as_view(), name='criarconta'),
    path('perfil/editar/', EditarPerfil.as_view(), name='editarperfil'),
    path('check_email/', check_user_email, name='check_email'),

]


