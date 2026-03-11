# Mini Blog de Curiosidades

Um mini blog feito em **Django** para compartilhar curiosidades sobre tecnologia, internet, astronomia e outros temas interessantes. O projeto possui funcionalidades de busca, filtragem por categoria, paginação e modo escuro.

---

## Funcionalidades

- Listagem de curiosidades com destaque por categoria.
- Busca por título de curiosidade.
- Filtro por categorias e ordenação.
- Paginação de 6 curiosidades por página.
- Modo escuro ativável pelo usuário.
- Página de detalhe de cada curiosidade.
- Destaque de termos pesquisados.

---

## Tecnologias

- Python 3.11+
- Django 5.2.8
- HTML, CSS e JS (para front-end)
- Bibliotecas adicionais:
  - BeautifulSoup4
  - Requests
  - Python-Decouple / Python-Dotenv
  - Whitenoise (para deploy)
  - Gunicorn (para deploy em servidor Linux)

---

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/gabrielbastosg/Mini-Blog-Curiosidade.git
cd Mini-Blog-Curiosidade

Crie um ambiente virtual (recomendado):

python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows

Instale as dependências:

pip install -r requirements.txt

Faça as migrações do Django:

python manage.py migrate

Crie um superusuário (opcional, para o admin):

python manage.py createsuperuser

Execute o servidor local:

python manage.py runserver

Estrutura do projeto
Mini-Blog-Curiosidade/
├── curiosidades/        # App Django principal
├── db.sqlite3           # Banco de dados SQLite (não enviado para o GitHub)
├── manage.py
├── requirements.txt
├── static/
├── templates/
└── README.md

Licença

Projeto livre para aprendizado e uso pessoal.
