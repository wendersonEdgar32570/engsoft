from datetime import datetime

def mostraLinha ():
    print(150*'*')



def cadastroCliente():
    try:
        nomeVendedor = input("digite o nome do vendedor: ")
        nomeCliente = input("digite o nome do cliente:  ")
        endCliente = input("digite o endereço do cliente:  ")
        telefoneCliente = int(input("digite o telefone do cliente: "))
        mostraLinha()
        print('relatorio de cadastro')
        mostraLinha()
        print(" vededor: {} \n Cliente: {} \n endereço: {}\n telefone: {}".format(nomeVendedor,nomeCliente,endCliente,telefoneCliente))
        mostraLinha()
        if telefoneCliente != int():
            print("digite o numero de telefone valido")
            cadastroCliente()
        else:
            print("o programa segue livre ")
    except ValueError:
        mostraLinha()
        print("ATENÇÃO VOCÊ DEVE DIGITAR NUMEROS INTEIROS NO CAMPO 'DIGITE O TELEFONE DO CLIENTE' ")
        mostraLinha()

mostraLinha()
print("sistema de cadastro")
mostraLinha()
cadastroCliente()
mostraLinha()
print("fim do programa")
mostraLinha()



