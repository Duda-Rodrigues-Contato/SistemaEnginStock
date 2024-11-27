#Responsável: Gabriel Calado

import json
import os
import re
from menus import *
from uteis import *

#import os
#import json
#import re

arquivo_clientes = "SistemaEnginStock/apresentacao/DataBase/clientes.json"
#caminho_arquivo = "D:/GitHub/studies-python/Cesar/trabalho aeda clientes/clientes.json"

def buscar_cliente_por_cnpj():
   
    if os.path.exists(caminho_arquivo) and os.path.getsize(caminho_arquivo) > 0:
        with open(caminho_arquivo, "r") as arquivo:
            dados_existentes = json.load(arquivo)
    else:
        print("Nenhum cliente encontrado.")
        return

    cnpj_cliente = input("Digite o CNPJ do cliente que deseja buscar (somente números): ")
    cnpj_cliente = re.sub(r'[^0-9]', '', cnpj_cliente)  # Remove caracteres não numéricos

    if not (cnpj_cliente.isdigit() and len(cnpj_cliente) == 14):
        print("CNPJ inválido. Certifique-se de que contém 14 dígitos numéricos.")
        return

    cliente_encontrado = False
    for cliente in dados_existentes:
        if cliente["cnpj"] == cnpj_cliente:
            cliente_encontrado = True
            cnpj_formatado = f"{cliente['cnpj'][:2]}.{cliente['cnpj'][2:5]}.{cliente['cnpj'][5:8]}/{cliente['cnpj'][8:12]}-{cliente['cnpj'][12:]}"
            print("\nCliente encontrado:")
            print(f"Nome: {cliente['nome']}")
            print(f"CNPJ: {cnpj_formatado}")
            print(f"Telefone: {cliente['telefone']}")
            print("-" * 30)
            break

    if not cliente_encontrado:
        print("\nCliente com o CNPJ especificado não encontrado.")


def menu():
    
    print("\nMenu de Opções:")
    print("1. Cadastrar cliente")
    print("2. Atualizar cliente")
    print("3. Deletar cliente")
    print("4. Listar clientes")
    print("5. Buscar cliente por CNPJ")
    print("6. Sair")

def main():
    while True:
        menu()
        opcao = input("Digite o número da opção desejada: ").strip()

        if opcao == "1":
            create_client()
        elif opcao == "2":
            update_client()
        elif opcao == "3":
            delete_client()
        elif opcao == "4":
            list_clients()
        elif opcao == "5":
            buscar_cliente_por_cnpj()
        elif opcao == "6":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
