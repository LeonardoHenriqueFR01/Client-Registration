# Flask Client Management System

## 📌 Sobre o Projeto
Este é um sistema de gerenciamento de clientes desenvolvido com Flask. Ele permite que usuários realizem login e gerenciem cadastros de clientes de forma segura e eficiente.

## 🛠 Tecnologias Utilizadas
- Python
- Flask
- SQLite 
- HTML, CSS, JavaScript (para a interface)

## 🚀 Funcionalidades
- 🔐 **Sistema de Login**: Registro e autenticação de usuários.
- 📋 **Cadastro de Clientes**: Adicionar, editar e excluir clientes.
- 🔍 **Listagem de Clientes**: Visualizar clientes cadastrados.

## 📂 Estrutura do Projeto
```
/app
│-- main.py
│-- __init.py__
│-- requirements.txt
│-- /templates
│   │-- index.html
│   │-- login.html
│   │-- register.html
│   │-- dashboard.html
│-- /static
│   │-- /css
│   │-- /js
│-- /models
│-- /routes
│-- /instance
```

## 📦 Como Executar o Projeto
### 1️⃣ Clone o Repositório
```bash
git https://github.com/LeonardoHenriqueFR01/Client-Registration.git
cd projeto-flask
```
### 2️⃣ Crie um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```
### 3️⃣ Instale as Dependências
```bash
pip install -r requirements.txt
```
### 4️⃣ Execute o Aplicativo
```bash
python main.py
```
Acesse `http://127.0.0.1:5000/` no navegador.

## 🔒 Segurança
- As senhas são armazenadas de forma segura utilizando hashing.
- Rotas protegidas para evitar acessos não autorizados.

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se livre para modificá-lo e utilizá-lo conforme necessário.

---
✉️ Caso tenha dúvidas ou sugestões, entre em contato! 🚀
