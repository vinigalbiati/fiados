fiadores = [];
divida = [];

def mostrar_fiadores():
    print("Fiadores atuais: ")
    if(len(fiadores) == 0):
        print("Lista de fiadores vazia! ")
    else:
        for i in range(len(fiadores)):
            print(i,"--"," Fiador:",fiadores[i], "-- Divida: ",divida[i], end="\n")

def adicionar_fiado():
    mostrar_fiadores()
    while True:
        fiadores.append(input("Digite o nome do fiador: (Digite * para sair) "));
        if(fiadores[-1] == "*"):
            del fiadores[-1]
            break
            
        divida.append(int(input("Digite a divida do fiador: ")));
        check_adicionar_fiado = input("Deseja adicionar mais algum fiador? S/N ");
        if check_adicionar_fiado == "N":
            break;
        else:
            continue;
    for i in range(len(fiadores)):
        print(i,"--"," Fiador:",fiadores[i], "-- Divida: ",divida[i], end="\n")
    else:
        menu()

def pagar_fiado():
    if(len(fiadores) == 0):
        print("Não há ninguem para excluir o fiado:")
        menu()
    else:
        mostrar_fiadores()
        cod_fiado = int(input("Digite o codigo do fiador que pagou: "))
        del fiadores[cod_fiado]
        mostrar_fiadores()
        menu()


def menu():
    print("-----MENU SALGADO-----")
    print("1 - Adicionar salgado")
    print("2 - Adicionar fiado")
    print("3 - Pagar fiado")
    print("---------------------")
    opcao = int(input("Digite uma opção: "))
    if(opcao == 2):
        adicionar_fiado()
    elif(opcao == 3):
        pagar_fiado()

menu()
    




