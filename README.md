## AgroLog API

Sistema back-end para registro e acompanhamento de atividades no campo, com autenticação segura utilizando JWT.

---

## Objetivo

O AgroLog foi desenvolvido para auxiliar produtores no controle das atividades agrícolas, permitindo registrar eventos diários, problemas na lavoura e ações tomadas, mantendo um histórico organizado por propriedade.

---

## Funcionalidades

* 🔐 Autenticação com JWT (login seguro)
* 👨‍🌾 Cadastro de usuários
* 🏡 Cadastro de propriedades
* 📓 Registro diário de atividades no campo
* 📊 Histórico de registros por propriedade

---

## Tecnologias utilizadas

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL (ou Oracle)
* JWT (python-jose)
* Bcrypt (passlib)
* Git e GitHub

---

## Autenticação

A API utiliza autenticação baseada em token JWT.

### Fluxo:

1. Usuário se registra (`/register`)
2. Realiza login (`/login`)
3. Recebe um token JWT
4. Utiliza o token nas requisições protegidas

### Exemplo de uso:

Authorization: Bearer SEU_TOKEN_AQUI

---

## Endpoints principais

### 🔐 Auth

* POST /register
* POST /login

### Propriedades

* GET /propriedades
* POST /propriedades

### Registros

* GET /registros
* POST /registros

## 📌 Status do Projeto
Início - 13/04/2026

Status: Em desenvolvimento

## 👨‍💻 Autor

Desenvolvido por Caio Fabrício D'Olivo Almeida
Cursando Análise e Desenvolvimento de Sistemas - UNICESUMAR