from mysql.connector import connect

if __name__ == "__main__":
    print("Tentando conectar o banco de dados!!")

    conexao = connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="admin",
        database="super_empresa"
    )
    print("Conexão realizada com sucesso")
    #Criar um cursor que nos permitirá executar comandos  no banco de dados
    cursor = conexao.cursor()
    # Definir qual será o comando que iremos executar, neste caso será um insert
    cursor.execute("insert into produtos (nome) values ('X-calabresa')")
    cursor.execute("insert into produtos (nome) values ('X-Bacon')")

    # Commit é nescessário pois sem ele o insert n será concretizado no bd
    conexao.commit()
    # Fechar a conexão com o db
    conexao.close()
    print("Produto cadastrado com sucesso")