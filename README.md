# Cadastro de Usuário - Django

Este é o meu primeiro projeto utilizando o framework Django. O objetivo é criar um sistema simples de cadastro de usuários, com um banco de dados integrado, onde é possível registrar informações como id, nome, e-mail, CPF e data de nascimento dos usuários.

## Funcionalidades

- **Cadastro de usuário**: O projeto permite cadastrar novos usuários com as informações:
  - ID (gerado automaticamente pelo banco de dados)
  - Nome
  - E-mail
  - CPF
  - Data de Nascimento
- **Conexão com banco de dados**: O sistema utiliza um banco de dados para armazenar as informações dos usuários.
- **Validação de dados**: Algumas validações básicas, como o formato do e-mail e CPF, são realizadas.

## Tecnologias Utilizadas

- **Django**: Framework web para o desenvolvimento do projeto.
- **SQLite**: Banco de dados utilizado (padrão do Django, ideal para este tipo de projeto simples).
- **Python**: Linguagem de programação utilizada no desenvolvimento.

## Estrutura do Projeto

- models.py: Onde a estrutura do banco de dados (modelo de usuário) é definida.
- views.py: Controla a lógica de exibição e interação do sistema.
- urls.py: Define as rotas para acessar as páginas do projeto.
- templates: Contém os arquivos HTML que renderizam as páginas.

## Conclusão 

Esse projeto é simples, mas representa um excelente ponto de partida para entender a integração do Django com banco de dados e a construção de sistemas básicos de cadastro de usuários. Ele mostra minhas habilidades iniciais com o Django e a criação de aplicações web dinâmicas.