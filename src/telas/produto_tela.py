import questionary
from src.repositorios import produto_repositorio
def executar_produto():
    opcoes = ["Lista todos", "cadastrar", "Editar", "Apagar", "Voltar"]
    opcao_desejada = ""
    while opcao_desejada != "Voltar":
         opcao_desejada = questionary.select("Escolha o menu desejado dos produtos", opcoes).ask()
         if opcao_desejada == "cadastrar":
            __cadastrar()
         elif opcao_desejada == "Listar todos":
             __listar_todos()  

def __listar_todos():
    produtos = produto_repositorio.listar_todos()
    print("Lista de produtos:")
    for produto in produtos:
        print("Id:", produto["id"], "Nome:", produto["nome"])              

# Função com um/dois underlines(s)antes do nome são consideradas
# Função privadas, ou seja, não devem/podem ser utilizadas em outros
# Arquivos
def __cadastrar():
     # Função responsável por cadastrar um produto, solicitando os dados
     # Nescessários para o cadastro
     nome_produto = input("Digite o nome do produto: ")    

     # Chama a função de cadastrar(insert) o produto no db
     # passando como parâmetro o nome do produto
     produto_repositorio.cadastrar(nome_produto)

     print("produto cadastrado com Sucesso!!!")
