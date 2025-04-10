import sys
from mysql.connector import connect

def abrir_conexao():
    try:
        conexao = connect(
                host="127.0.0.1",  # host é a maquina que está o banco de dados 
                port=3306,         # porta padrão do mysql
                user="root",       # usuario 
                password="admin",
                database="super_empresa"
            )
        return conexao
    except Exception as  erro:
        print("Não foi possivel reaizar a conexão com o banco de dados")
        print(erro)
        # Encerra a aplicação por completo com um status code:
        # 0 sucesso, ou seja, a aplicação foi executada com sucesso
        # 1 erro
        sys.exit(1)