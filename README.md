# Projeto HashFlix

Esta é uma aplicação web baseada em Django que simula uma plataforma de streaming de filmes (como a Netflix). Ela permite aos usuários navegar por filmes, ver detalhes, pesquisar, criar contas, fazer login e editar seus perfis.

## Instruções de Configuração

Siga estes passos para configurar e executar o projeto HashFlix em sua máquina local.

### 1. Clonar o Repositório

Se ainda não o fez, clone este repositório para sua máquina local:

```bash
git clone <url_do_repositorio>
cd HashFlix
```

### 2. Criar um Ambiente Virtual (Recomendado)

É altamente recomendável usar um ambiente virtual para gerenciar as dependências do projeto.

```bash
python -m venv venv
```

### 3. Ativar o Ambiente Virtual

- **No Windows:**
  ```bash
  .\venv\Scripts\activate
  ```
- **No macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Instalar Dependências

Instale todos os pacotes Python necessários usando `pip`:

```bash
pip install -r requirements.txt
```
*(Nota: Se encontrar problemas com o Pillow, certifique-se de ter as bibliotecas de processamento de imagem necessárias instaladas em seu sistema, por exemplo, `sudo apt-get install libjpeg-dev zlib1g-dev` no Debian/Ubuntu.)*

### 5. Aplicar Migrações

Execute as migrações do Django para configurar o esquema do banco de dados:

```bash
python manage.py makemigrations filme
python manage.py migrate
```

### 6. Criar um Superusuário (Conta de Administrador)

Crie uma conta de administrador para acessar o painel de administração do Django e gerenciar o conteúdo:

```bash
python manage.py createsuperuser
```
Siga as instruções para configurar seu nome de usuário, e-mail e senha.

### 7. Iniciar o Servidor de Desenvolvimento

Finalmente, inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

A aplicação deve agora estar acessível em seu navegador web em `http://127.0.0.1:8000/`.

## Correções e Melhorias Recentes

- **Problema de Verificação CSRF:** Resolvido causas comuns de falhas na verificação CSRF (Cross-Site Request Forgery), garantindo que todos os formulários em `login.html`, `criarconta.html` e `editarperfil.html` incluam corretamente a tag de template `{% csrf_token %}`.
- **Indentação de Métodos de View:** Corrigida a indentação inadequada dos métodos `get_success_url` dentro das views baseadas em classe `CriarConta` e `EditarPerfil` em `filme/views.py`. Isso garante o redirecionamento adequado após o envio de formulários.

---
**Nota para Desenvolvedores:**

- **Versão do Django:** Este projeto foi desenvolvido com Django 5.0.1.
- **Versão do Python:** Certifique-se de estar usando uma versão compatível do Python.
