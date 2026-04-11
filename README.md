markdown
# 📘 Agenda de Eventos – Projeto Django

Este projeto foi desenvolvido como parte do curso de **Django da plataforma DIO (Digital Innovation One)**, no qual foram explorados os conceitos fundamentais do framework e construído um sistema completo de agenda de eventos com autenticação, inserção, edição, exclusão e exibição dinâmica de dados.

## 🎯 Objetivo do Projeto

Criar uma aplicação web simples, porém funcional, utilizando Django, permitindo ao usuário:

- Realizar login e logout  
- Criar novos eventos  
- Listar eventos existentes  
- Editar eventos já cadastrados  
- Excluir eventos  
- Visualizar histórico de eventos  
- Exibir dinamicamente eventos próximos e atrasados  

---

## 🧠 Conteúdos Aprendidos no Curso (Módulos)

### **1️⃣ Introdução aos conceitos e ambientes do Django**  
Configuração inicial do ambiente, criação de projeto e aplicações, entendimento da arquitetura MTV.

### **2️⃣ Estrutura básica e introdução de dados com o Django Admin**  
Modelagem no Django ORM, criação de tabelas, cadastro e administração de dados pelo admin.

### **3️⃣ Criando uma página de listagem**  
Templates, fluxo request/response, exibição de dados dinâmicos na interface HTML.

### **4️⃣ Autenticação e inserção de dados**  
Sistema de login, proteção com CSRF, formulários, processamento de POST e validações.

### **5️⃣ Alterando, excluindo e filtrando dados no banco**  
Operações CRUD completas, filtragens, renderização de mensagens, manipulação avançada com ORM.

---

## 🛠 Tecnologias Utilizadas

- **Python 3.x**  
- **Django**  
- **HTML5**  
- **CSS3** (com tema em tons pastéis)  
- **Visual Studio Code (VSCode)**  

---

## 📂 Funcionalidades da Aplicação

- Autenticação de usuários (login/logout)  
- Cadastro de novos eventos  
- Edição e exclusão de eventos  
- Listagem principal com destaque para eventos:  
  - **Vencidos** (vermelho)  
  - **Próximos em até 1 hora** (amarelo)  
- Histórico de eventos  
- Layout responsivo com header, footer e páginas padronizadas  

---

## 📸 Estrutura Visual

A aplicação foi estilizada inteiramente com CSS manual, **com o auxílio de inteligência artificial**, incluindo:

- Páginas com tons pastéis  
- Formulários estilizados  
- Botões personalizados  
- Cards para exibição de eventos  
- Templates base reutilizáveis (`model-page`, `model-header`, `model-footer`)  

---

## 👤 Autor

Desenvolvido por **Lucas Feitosa Rossinhole**.  
LinkedIn: **https://www.linkedin.com/in/lfrossinhole/**  

---

## 🚀 Como executar o projeto

```bash
# Clone o repositório
git clone 

# Acesse o diretório do projeto
cd nome_do_projeto

# Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver

Acesse em: **http://127.0.0.1:8000/**  

---

## ✔ Observações

Este projeto tem foco didático e cumpre o propósito de aplicar na prática os conceitos iniciais do Django.  
Foi construído do zero durante o aprendizado e refatorado posteriormente com melhorias visuais e de organização.
```