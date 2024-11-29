#Responsável: Gabriel Calado

import json
import os
import re
from uteis import *

arquivo_clientes = "SistemaEnginStock/apresentacao/DataBase/clientes.json"

def create_client():
    cliente = ler_arquivo(arquivo_clientes)

    while True:
        while True:
            cnpj = input("Digite o CNPJ do cliente (14 dígitos): ")
            cnpj = re.sub(r'[^0-9]', '', cnpj)
            if not (cnpj.isdigit() and len(cnpj) == 14):
                print("CNPJ inválido. Certifique-se de que contém 14 dígitos numéricos.")
                continue
            if any(cliente["cnpj"] == cnpj for cliente in dados_existentes):
                print("Já existe um cliente com esse CNPJ. Digite um CNPJ diferente.")
            else:
                break

        while True:
            telefone = input("Digite o telefone do cliente (9 dígitos, começando com 9): ")
            if not (telefone.isdigit() and len(telefone) == 9 and telefone.startswith('9')):
                print("Telefone inválido. Certifique-se de que contém 9 dígitos e comece com 9.")
                continue
            if any(cliente["telefone"] == telefone for cliente in dados_existentes):
                print("Já existe um cliente com esse telefone. Digite um telefone diferente.")
            else:
                break

        cliente = {
            "nome": input("Digite o nome do cliente: "),
            "cnpj": cnpj,
            "telefone": telefone
        }

        escrever_arquivo(arquivo_clientes, cliente)

        print("\nCliente salvo com sucesso:")
        print(f"Nome: {cliente['nome']}")
        print(f"CNPJ: {cliente['cnpj']}")
        print(f"Telefone: {cliente['telefone']}")

        continuar = input("\nDeseja cadastrar outro cliente? (s/n): ").strip().lower()
        if continuar != 's':
            print("Cadastro encerrado.")
            break


def update_client():

    cliente = ler_arquivo(arquivo_clientes)

    while True:
        cnpj_cliente = input("Digite o CNPJ do cliente que deseja atualizar (ou 'sair' para cancelar): ")
        if cnpj_cliente.lower() == 'sair':
            print("Operação cancelada.")
            return
        
        cnpj_cliente = re.sub(r'[^0-9]', '', cnpj_cliente)
        
        cliente_encontrado = False
        for cliente in dados_existentes:
            if cliente["cnpj"] == cnpj_cliente:
                cliente_encontrado = True
                print("\nCliente encontrado. Deixe em branco para manter o valor atual.")
                
                cliente["nome"] = input(f"Nome [{cliente['nome']}]: ") or cliente["nome"]
                
                while True:
                    novo_cnpj = input(f"CNPJ [{cliente['cnpj']}]: ") or cliente["cnpj"]
                    novo_cnpj = re.sub(r'[^0-9]', '', novo_cnpj)
                    if not (novo_cnpj.isdigit() and len(novo_cnpj) == 14):
                        print("CNPJ inválido. Certifique-se de que contém 14 dígitos numéricos.")
                        continue
                    cliente["cnpj"] = novo_cnpj
                    break

                while True:
                    novo_telefone = input(f"Telefone [{cliente['telefone']}]: ") or cliente["telefone"]
                    if not (novo_telefone.isdigit() and len(novo_telefone) == 9 and novo_telefone.startswith('9')):
                        print("Telefone inválido. Certifique-se de que contém 9 dígitos e comece com 9.")
                        continue
                    cliente["telefone"] = novo_telefone
                    break
                
                escrever_arquivo(arquivo_clientes, cliente)

                print("\nCliente atualizado com sucesso!")
                print(f"Nome: {cliente['nome']}")
                print(f"CNPJ: {cliente['cnpj']}")
                print(f"Telefone: {cliente['telefone']}")

                return cliente
        
        if not cliente_encontrado:
            print("Cliente com CNPJ especificado não encontrado. Tente novamente.")

def delete_client():

    cliente = ler_arquivo(arquivo_clientes)

    cnpj_cliente = input("Digite o CNPJ do cliente que deseja excluir: ")

    cnpj_cliente = re.sub(r'[^0-9]', '', cnpj_cliente)

    if not (cnpj_cliente.isdigit() and len(cnpj_cliente) == 14):
        print("CNPJ inválido. Certifique-se de que contém 14 dígitos numéricos.")
        return

    cliente_encontrado = False
    for i, cliente in enumerate(dados_existentes):
        if cliente["cnpj"] == cnpj_cliente:
            cliente_encontrado = True
            del dados_existentes[i]
            print(f"\nCliente com CNPJ {cnpj_cliente} excluído com sucesso.")
            break

    if not cliente_encontrado:
        print("Cliente com o CNPJ especificado não encontrado.")
        return

    escrever_arquivo(arquivo_clientes, cliente)

def list_clients():

    cliente = ler_arquivo(arquivo_clientes)

    if not cliente:
        print("NENHUM CLIENTE CADASTRADO!")
    else:
        listar()
        for cnpj, dados in cliente.items():
            print(f"Nome: {dados['nome']}")
            print(f"CNPJ: {dados['cnpj']}")
            print(f"Telefone: {dados['telefone']}")
            print()
            print()


def buscar_cliente():

    cliente = ler_arquivo(arquivo_clientes)

    encontrado = False
    busca = input("Digite o nome ou o CNPJ do cliente que deseja buscar: ")
    validar_cnpj(busca)

    if not cliente:
        print("NENHUM CLIENTE CADASTRADO!")
    else:
        for busca, dados in cliente.items():
            if cliente['cnpj'] == busca:
                print(f"Nome: {dados['nome']}")
                print(f"CNPJ: {dados['cnpj']}")
                print(f"Telefone: {dados['telefone']}")
                print()
                print()
                encontrado = True