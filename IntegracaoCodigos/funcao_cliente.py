#Funções da Área de Clientes (5 setor do menu principal).

import json
import os
from time import sleep
from menus.menus import menu_clientes
import re

class cor:
    NEGRITO = '\033[1m'
    AZUL = '\033[44m'
    RESET = "\033[0m"

cont_cnpj = 0
cont_ddd = 0
cont_telefone = 0
caminho_arquivo_cliente = os.path.join(os.path.dirname(__file__), 'clientes.json')
dados_clientes = []
cliente = {}

#5.1. Cadastrar Clientes. (create_client)
#5.2. Listar Clientes. (list_client)
#5.3. Alterar Dados de Clientes. (update_client)
#5.4. Deletar Cliente. (delete_client)
#5.5. Voltar.
#5.6. Encerrar Sistema.

def criar_arquivo_json():
    if not os.path.exists(caminho_arquivo_cliente):
        with open(caminho_arquivo_cliente, 'w') as arquivo_clientes:
            json.dump({}, arquivo_clientes, indent=4)

    with open(caminho_arquivo_cliente, 'r') as arquivo_clientes:
        return json.load(arquivo_clientes)

def creat_clients():

    cliente = criar_arquivo_json()

    while True:
        
        while True: 

            cnpj_cliente = int(input("Digite o CNPJ do cliente SEM caracter especial: "))
            cnpj_cliente = str(cnpj_cliente)

            if not len(cnpj_cliente) == 14:

                print("CNPJ Inválido!")
                print("Você tem mais 3 tentativas.")

                while cont_cnpj <= 3:

                    cont_cnpj += 1
                    cnpj_cliente  = int(input("Digite o CNPJ do cliente SEM caracter especial: "))

                    if not len(cnpj_cliente) == 14:

                        cont_cnpj += 1
                        print("1 tentativa A MENOS!")

                        if cont_cnpj == 3:

                            print("Você chegou ao número MÁXIMO de tentativas.")
                            print("Encerrando Sistema...")
                            sleep(2.5)
                            break

                    else: 

                        break
            else: 

                break
        
        while True:

            #DDD's existentes no Brasil: 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99
            lista_DDD = [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99]
            
            ddd_cliente = int(input("Digite o DDD do número de telefone do cliente SEM caracter especial:"))

            if not ddd_cliente in lista_DDD:

                print("DDD Inválido!")
                print("Você tem mais 3 tentativas.")

                while cont_ddd <= 3:

                    cont_ddd += 1
                    ddd_cliente = int(input("Digite o DDD do número de telefone do cliente SEM caracter especial (2 números):"))

                    if not ddd_cliente in lista_DDD:

                        cont_ddd += 1
                        print("1 tentativa A MENOS!")

                        if cont_ddd == 3:

                            print("Você chegou ao número MÁXIMO de tentativas.")
                            print("Encerrando Sistema...")
                            sleep(2.5)
                            break
                    
                    else:

                        break
            else:

                break
        
        while True:

            telefone_clientes = int(input("Digite o número de telefone do cliente SEM DDD e SEM caracter especial (9 números): "))
            telefone_clientes = str(telefone_clientes)

            if not len(telefone_clientes) == 9:

                print("Número de Telefone Inválido!")
                print("Você tem mais 3 tentativas.")

                while cont_telefone <= 3:

                    cont_telefone += 1
                    telefone_clientes = int(input("Digite o número de telefone do cliente SEM DDD e SEM caracter especial (9 números): "))
                    telefone_clientes = str(telefone_clientes)
                    
                    if not len(telefone_clientes) == 9:
                        
                        cont_telefone += 1
                        print("1 tentativa A MENOS!")

                        if cont_telefone == 3:

                            print("Você chegou ao número MÁXIMO de tentativas.")
                            print("Encerrando Sistema...")
                            sleep(2.5)
                            break

                    else:

                        break

            else:

                break

        nome_cliente = input("Digite o nome do cliente: ")

        cliente = {
            "nome": nome_cliente,
            "cnpj": cnpj_cliente,
            "telefone": telefone_clientes
        }

        dados_clientes.append(cliente)

        with open(caminho_arquivo_cliente, 'w') as arquivo_cliente:
            json.dump(dados_clientes, arquivo_cliente, indent=4)

        print("Cliente Adicionado!")
        print("Encerrando Sistema...")
        sleep(2.5)
        break

def list_client():
    
    cliente = criar_arquivo_json()

    if cliente:
        
        os.system('cls')
        print("|" + " " + "=" * 60 + " " + "|")
        print("|" + " " + '-' * 60 + " " + "|")
        print("|" + " " + cor.NEGRITO + cor.AZUL + "SISTEMA ENGINSTOCK:" + cor.RESET + " " * 42 + "|")
        print("|" + " " + '-' * 60 + " " + "|")
        print("|" + " " + "=" * 60 + " " + "|")
        print("|" + " " + '-' * 60 + " " + "|")
        print("|" + " " + cor.NEGRITO + "Lista de Clientes:" + cor.RESET + " " * 44 + "|")
        print("|" + " " + " " * 61 + "|")

        for usuario_cadastrados in cliente:
            print(f"Nome do Cliente: {cliente['nome_cliente']}")
            print(f"CNPJ do Cliente: {cliente['cnpj_cliente']}")
            print(f"Número de Telefone do Cliente: {cliente['telefone_clientes']}") 
    else:

        print("Nenhum Cliente Cadastrado!")

list_client()