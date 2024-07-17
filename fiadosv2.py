cliente_nome = {}

class clientes:
    def __init__(self, nome, divida, anoCurso):
        self.nome = nome
        self.divida = divida
        self.anoCurso = anoCurso

def adicionar_fiado():
    opcao_add = input('''1 - Adicionar novo cliente
          2 - Adicionar novo fiado ao cliente \n''')
    if(opcao_add == '1'):
        nome = input("Qual o nome do cliente: ")
        divida = int(input("Qual a divida do cliente: "))
        anoCurso = input("Em qual ano o cliente está: ")
        cliente_nome[nome] = clientes(nome, divida, anoCurso)
        ver_fiadores()
        menu()
    elif(opcao_add == '2'):
        ver_fiadores()
        nome = input('Digite o nome do fiador a adicionar divida: ')
        divida = int(input('Digite a divida a ser adicionada: '))
        cliente_nome[nome].divida += divida
        ver_fiadores()
        menu()
    

        

def remover_fiado():
    nome = input("Digite o nome do fiador a remover a divida: ")
    while nome not in cliente_nome:
        print("O fiador digitado nao existe")
        nome = input("Digite o nome do fiador a remover a divida: ")
    divida = int(input("Digite a divida a ser removida: "))
    if(divida >= cliente_nome[nome].divida):
        del cliente_nome[nome]
        print("Fiador removido")
    else:
        cliente_nome[nome].divida -= divida
    ver_fiadores()
    menu()

def ver_fiadores():
    for pessoas in cliente_nome:
        print(f'Nome do fiador: {cliente_nome[pessoas].nome}\nDivida atual: {cliente_nome[pessoas].divida}')



def menu():
    print('''\nDigite um numero para acessar as funções do app:
          1 - Adicionar fiado
          2 - Remover fiado
          3 - Ver fiadores
          4 - Fechar programa \n''')
    opcao_menu = input()
    match opcao_menu:
        case "1":
            adicionar_fiado()
        case "2":
            remover_fiado()
        case "3":
            ver_fiadores()
        case "4":
            exit()
        case _:
            print("Opção inválida")
            menu()
    
menu()
