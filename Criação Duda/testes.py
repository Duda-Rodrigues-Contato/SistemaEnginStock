#Arquivo python para testes ligao ao arquivo "testes.json".

import json
import os

#add_compra = {}

#cadastrar = os.path.join(os.path.dirname(__file__), "testes.json")

#if not os.path.exists(cadastrar):
    #with open(cadastrar, "w") as f:
        #json.dump([], f, indent = 4)


#1 - Dicionário em python.
#Variaveis: 
# - código da compra p/ entrar em deletar compra
# - tempo de entrega da compra
# - nome(s) do(s) produto(s) da compra e qtd de cada produto

#with open(cadastrar, "r") as f:
    #add_compra = json.load(f)

#codigo = int(input("Digite o código da compra: "))
#tempo_entrega = int(input("Digite o tempo de entrega em DIAS: "))

#add_compra.append(codigo, tempo_entrega)

#with open(cadastrar, "w") as f:
    #add_compra = json.dump(f)

class Gerenciador():

    def iniciacao():

        global cadastrar
        cadastrar = os.path.join(os.path.dirname(__file__), 'testes.json')
        if not os.path.exists(cadastrar):
            with open(cadastrar, 'w') as f:
                json.dump({}, f)


    def adicionar_compra(codigo_compra, tempo_entrega, nome_produto, qtd_produto):

        with open(cadastrar, 'r') as f:
            compras = json.load(f)

        compras.append({'codigo_compra':codigo_compra, 'tempo_entrega':tempo_entrega, 'nome_produto':nome_produto, 'qtd_produto':qtd_produto})

        with open(cadastrar, 'w') as f:
            json.dump(compras, f, indent=4)
        print("Compra Adicionada!")

def menu_principal():

    os.system('cls')
    print("=" * 50)
    print()
    print("-" * 50)
    print("ÁREA DE COMPRAS:")
    print("4.1 - Cadastrar Compra.") #Variaveis: tempo de entrega da compra, código da compra p/ entrar em deletar compra, nome(s) do(s) produto(s) da compra e qtd de cada produto
    print("4.2 - Listar Compras:.") #Criar outro menu p/ opção de período de compra (ex: 1 mês, 3 mês)
    print("4.3 - Atualizar Compra.") #Somente se o datetime não exceder o período de entrega do produto digitado na área "cadastrar compra".
    print("4.4 - Deletar Compra.")
    print("4.5 - Voltar.")
    print("4.6 - Encerrar Sistema.")
    print()
    print("=" * 50)


def main():

    gerenciador = Gerenciador()

    while True:

        menu_principal()

        escolha = int(input("Digite sua escolha: "))

        match escolha:
            case 1:

                codigo_compra = int(input("Digite o código da compra: "))
                tempo_entrega = int(input("Digite o tempo de entrega em DIAS: "))
                nome_produto = input("Digite o nome do produto: ")
                qtd_produto = int(input("Digite a qtd do produto: "))
                gerenciador.adicionar_compra(codigo_compra, tempo_entrega, nome_produto, qtd_produto)


main()