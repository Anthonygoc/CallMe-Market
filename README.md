# 📞 CallMe — Plataforma de Vendas com Django

Bem-vindo ao **CallMe**, um sistema web construído com Django 5 que simula uma plataforma de vendas profissional, no estilo do site da JetBrains. O objetivo é criar um ambiente onde usuários possam:

- Criar contas e fazer login/logout
- Visualizar produtos
- Realizar compras via integração com **Mercado Pago**
- Receber **promoções por e-mail**
- E mais!

---

## 🚀 Objetivo do Projeto

> O principal objetivo é desenvolver uma aplicação web completa com Django puro (sem frameworks JS externos), focando em **funcionalidade, segurança e usabilidade**, para simular uma plataforma de vendas real.

### Funcionalidades principais:

- 🧑 Cadastro, login, logout e perfil de usuário
- 📦 CRUD de produtos (público e via admin)
- 💳 Integração com **Mercado Pago** (checkout)
- 📧 Envio de promoções por e-mail
- 🛠️ Sistema administrável com Django Admin
- 🎨 Frontend responsivo com Bootstrap 5

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia       | Finalidade                         |
|------------------|------------------------------------|
| Django 5         | Framework backend e frontend       |
| SQLite           | Banco de dados padrão do Django    |
| Bootstrap 5      | Estilização frontend               |
| Mercado Pago API | Pagamento e checkout               |
| SMTP / Gmail     | Envio de e-mails promocionais      |

---

## 📁 Estrutura do Projeto
```bash
callme/
├── config/ # Configurações do projeto
├── myapp/ # App principal (views, templates, static)
│ ├── templates/
│ ├── static/
├── manage.py
├── db.sqlite3
```

---

## 📸 Telas planejadas

- Página inicial com produtos
- Tela de cadastro e login (com Bootstrap)
- Tela de checkout
- Área de perfil
- Página de confirmação de compra
- Área do admin (gestão de produtos e usuários)

---

## 🔒 Segurança

- Senhas protegidas por hash
- Proteção CSRF em todos os formulários
- Login protegido por sessão

---

## 📦 Instalação

```bash
git clone https://github.com/seu-usuario/callme.git
cd callme
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


