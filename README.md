Mini Blog de Curiosidades

Um mini blog desenvolvido com Django para compartilhar curiosidades sobre tecnologia, internet, astronomia e outros temas interessantes.

O projeto inclui funcionalidades como busca, filtragem por categoria, ordenação, paginação e modo escuro, servindo como prática de desenvolvimento web com Django.

Funcionalidades

Listagem de curiosidades com destaque por categoria

Busca por título de curiosidade

Filtro por categorias

Ordenação por data ou título

Paginação de 6 curiosidades por página

Página de detalhe de cada curiosidade

Destaque de termos pesquisados

Modo escuro ativável pelo usuário

Tecnologias Utilizadas

Python 3.11+

Django 5.2.8

HTML

CSS

JavaScript

Bibliotecas adicionais

BeautifulSoup4

Requests

Python-Decouple / Python-Dotenv

Whitenoise (para deploy)

Gunicorn (para deploy em servidor Linux)

Instalação

Clone o repositório:

git clone https://github.com/gabrielbastosg/Mini-Blog-Curiosidade.git
cd Mini-Blog-Curiosidade

Crie um ambiente virtual (recomendado):

python -m venv env

Ative o ambiente virtual:

Linux / Mac:

source env/bin/activate

Windows:

env\Scripts\activate

Instale as dependências:

pip install -r requirements.txt

Execute as migrações do Django:

python manage.py migrate

Crie um superusuário (opcional para acessar o admin):

python manage.py createsuperuser

Execute o servidor local:

python manage.py runserver

Acesse no navegador:

http://127.0.0.1:8000
Estrutura do Projeto
Mini-Blog-Curiosidade/
│
├── curiosidades/        # App Django principal
├── db.sqlite3           # Banco de dados SQLite
├── manage.py
├── requirements.txt
├── static/              # Arquivos CSS, JS e imagens
├── templates/           # Templates HTML
└── README.md
Objetivo do Projeto

Este projeto foi desenvolvido para praticar:

Desenvolvimento web com Django

Organização de templates

Manipulação de dados com busca e filtros

Implementação de paginação

Estruturação de um pequeno projeto web completo

Licença

Projeto livre para aprendizado e uso pessoal.
