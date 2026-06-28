# Guilherme Quartin Coelho — Projeto Django

Projeto desenvolvido em Django para a unidade curricular de Programação Web.

## Tecnologias utilizadas

* Python
* Django
* Django Ninja
* HTML
* CSS
* SQLite / PostgreSQL
* Cloudinary
* WhiteNoise
* Docker
* GitHub Actions

---

## Como lançar o servidor localmente

### 1. Abrir o terminal na pasta do projeto

A pasta correta é a que contém o ficheiro `manage.py`.

Exemplo:

```bash
cd Guilherme-Quartin-Coelho-a22309752
```

---

### 2. Lançar o servidor

```bash
python manage.py runserver
```

Depois de executar o comando, abrir no navegador:

```text
http://127.0.0.1:8000/
```

---

## Acesso ao painel de administração

O painel de administração do Django está disponível em:

```text
http://127.0.0.1:8000/admin/
```

### Conta de administrador

```text
Username: GuilhermeQuartinCoelho
Password: programaçãoweb26
```

Esta conta tem permissões de administração total no sistema.

---

## Conta com role `gestor_portfolio`

Existe também uma conta com o papel/função `gestor_portfolio`.

### Conta gestor_portfolio

```text
Username: Guilherme
Email: guiqcoelho@gmail.com
Password: programaçãoweb26
Role: gestor_portfolio
```

Esta conta permite aceder às funcionalidades associadas à gestão do portfólio.

---

## Funcionalidades principais

O projeto inclui:

* Página inicial do portfólio;
* Gestão de conteúdos do portfólio;
* Sistema de autenticação;
* Conta de administrador;
* Conta com role `gestor_portfolio`;
* Integração com API própria através de Django Ninja;
* Integração com API externa;
* Operações CRUD;
* Páginas HTML com estilização em CSS;
* Deploy com Docker e GitHub Actions.

---

## Comandos úteis

Verificar se o projeto tem erros:

```bash
python manage.py check
```

Criar novas migrações:

```bash
python manage.py makemigrations
```

Aplicar migrações:

```bash
python manage.py migrate
```

Criar superutilizador:

```bash
python manage.py createsuperuser
```

Lançar o servidor:

```bash
python manage.py runserver
```

---

## Autor

**Guilherme Quartin Coelho**
Número de estudante: **a22309752**
