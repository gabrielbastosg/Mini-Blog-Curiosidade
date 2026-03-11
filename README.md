# Mini Blog de Curiosidades

Um mini blog feito em **Django** que apresenta curiosidades sobre tecnologia, internet, astronomia e outros temas interessantes. Possui filtros por categoria, busca por título, ordenação e modo escuro.

---

## Funcionalidades

- Lista de curiosidades paginadas.
- Busca por título.
- Filtro por categoria.
- Ordenação por data ou título.
- Destaque de termos buscados.
- Página de detalhe de cada curiosidade.
- Modo claro e escuro (salva preferência do usuário).
- Responsivo para dispositivos móveis.

---

## Tecnologias

- **Python 3.x**  
- **Django 4.x**  
- **HTML5 / CSS3**  
- **JavaScript** (para modo escuro)

---

## Estrutura do Projeto


Mini-Blog-Curiosidade/
│
├─ curiosidades/
│ ├─ templates/curiosidades/
│ │ ├─ index.html
│ │ └─ detalhe.html
│ ├─ static/curiosidades/
│ │ └─ style.css
│ ├─ views.py
│ └─ models.py
│
├─ db.sqlite3 (removido do repositório, configurado no .gitignore)
├─ manage.py
├─ requirements.txt
└─ README.md


---

## Como rodar localmente

1. Clone o repositório:

```bash
git clone https://github.com/gabrielbastosg/Mini-Blog-Curiosidade.git
cd Mini-Blog-Curiosidade

Crie um ambiente virtual (opcional, mas recomendado):

python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows

Instale as dependências:

pip install -r requirements.txt

Execute as migrações do Django:

python manage.py migrate

Rode o servidor:

python manage.py runserver

Abra no navegador:
