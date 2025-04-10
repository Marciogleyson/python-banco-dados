# Estrutur do projeto

## src
Pasta `src` é a pasta `source`, ou seja, ond fica nossos `códigos-fonte` 

## src/database

Pasta que contém os arquivos:
-`estrutura.sql`: contém o arquivo de criação do banco de dados `MySQL`
-`banco_dados.py`: arquivo responsável por abrir a conexão com o banco de dados

## src/repositorios
Pasta que contém os arquivos responsáveis por executar os comandos no banco de dados, ou seja, é o local que executará `insert`, `update`, `delete`, `select`, etc.

## src/telas
Pasta que contém os arquivos responsáveis por interagir com o usuário e chamar a camada de `repositorio` para interagir com o banco de dados.