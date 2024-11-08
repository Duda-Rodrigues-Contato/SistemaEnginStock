#Desenvolvimento do menu de *COMPRAS*:

import os
import json
from datetime import datetime, timedelta
from time import sleep

continuar = "S"
cont_qtd_produtos = 0

cadastrar_compra = os.path.join(os.path.dirname(__file__), "cadastrarcompra.json") 

#Verificar se o arquivo existe:
def arquivo_cadastrar_compra():
    if not os.path.exists(cadastrar_compra):
        with open(cadastrar_compra, "w") as f:
            json.dump([], f, indent = 4)


def menu_inicial_compras():

    os.system('cls')
    print("=" * 50)
    print()
    print("-" * 50)
    print("ÁREA DE COMPRAS:")
    print("4.1 - Cadastrar Compra.") #Variaveis: tempo de entrega da compra, código da compra p/ entrar em deletar compra, nome(s) do(s) produto(s) da compra e qtd de cada produto
    print("4.2 - Listar Compras.") #Criar outro menu p/ opção de período de compra (ex: 1 mês, 3 mês)
    print("4.3 - Atualizar Compra.") #Somente se o datetime não exceder o período de entrega do produto digitado na área "cadastrar compra".
    print("4.4 - Deletar Compra.")
    print("4.5 - Voltar.")
    print("4.6 - Encerrar Sistema.")
    print()
    print("=" * 50)


def continuar():

    print("S - Continuar Adicionando.")
    print("N - Não Adicionar Mais.")


def cadastrar_compra(codigo_compra, tempo_entrega, nome_produto, qtd_produto):

    global add_compra
    add_compra = arquivo_cadastrar_compra()

    add_compra.append({
        "codigo_compra": {
            "nome_produto": nome_produto,
            "qtd_produto": qtd_produto,
            "tempo_entrega": tempo_entrega
        }
    })

    with open(cadastrar_compra,  "w") as f:
        json.dump(add_compra, f, indent=4)



def main():

    while True:

        menu_inicial_compras()
        print()
        escolha_menu_compras = int(input("Digite sua escolha: "))

        match escolha_menu_compras:

            case 1: #Cadastrar Compra.

                codigo_compra = int(input("Digite o código da compra: ")) 
                tempo_entrega = float(input("Digite o tempo de entrega em DIAS: "))
                
                cadastrar_compra(codigo_compra, tempo_entrega, nome_produto, qtd_produto)

                global qtd_produtos_total 
                qtd_produtos_total = int(float("Quantos produtos diferentes você comprou? ")) 

                while cont_qtd_produtos <= qtd_produtos_total:

                    cont_qtd_produtos += 1

                    nome_produto = input("Digite o nome do produto comprado: ")
                    qtd_produto = int(input("Digite a quantidade comprada desse produto: "))

                    cadastrar_compra(codigo_compra, tempo_entrega, nome_produto, qtd_produto)

                    if cont_qtd_produtos > qtd_produtos_total:
                        
                        print("Produtos Adicionados")
                        
                        sleep(2)

                        print("Encerrando Sistema!")
                        break
               
main()