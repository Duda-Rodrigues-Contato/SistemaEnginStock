import os
import re
from menus import *
from uteis import *

arquivo_compras = "SistemaEnginStock/apresentacao/DataBase/compras.json"

arquivo_existe(arquivo_compras)

def adicionar_compra():

    compras = ler_arquivo(arquivo_compras)

    while True:

        os.system('cls')

        codigo_compra = input("Digite o código da compra: ")
        validar_codigo(codigo_compra, compras)

        nome_produto = input("Digite o nome do produto comprado: ")
        qtd_produto = int(input("Digite quantas unidades do produto foram compradas: "))
        tempo_entrega = float(input("Digite o tempo de entrega em DIAS: "))
        preco_compra = float(input("Digite o valor total da compra: "))
        cnpj_fornecedor_compra = input("Digite o CNPJ do fornecedor que a compra foi feita: ")
        validar_cnpj(cnpj_fornecedor_compra)

        preco_unitario = preco_compra // qtd_produto 

        compras[codigo_compra] = {
            'nome_produto': nome_produto,
            'qtd_produto': qtd_produto,
            'tempo_entrega': tempo_entrega,
            'preco_compra': preco_compra,
            'preco_unitario': preco_unitario,
            'cnpj_fornecedor_compra': cnpj_fornecedor_compra
        }

        escrever_arquivo(arquivo_compras, compras)
        print(f"COMPRA {codigo_compra} ADICIONADA COM SUCESSO!")


def listar_compras():

    compras = ler_arquivo(arquivo_compras)

    if not compras:
        print("NENHUMA COMPRA CADASTRADA!")
    else:
        listar()
        for codigo_compra, dados in compras.items():
            print("       " + f"Código da Compra: {codigo_compra}.")
            print("       " + f"Nome do Produto: {dados['nome_produto']}.")
            print("       " + f"Preço Unitário: {dados['preco_unitario']}.")
            print("       " + f"Preço Total da Compra: {dados['preco_compra']}.")
            print("       " + f"Quantidade: {dados['qtd_produto']}.")
            print("       " + f"Tempo de Entrega: {dados['tempo_entrega']}.")
            print()
            print()


def buscar_compra():

    compras = ler_arquivo(arquivo_compras)

    codigo_compra = input("Digite o código da compra: ")

    encontrado = False

    if not compras:
        print("NENHUMA COMPRA CADASTRADA!")
    else:
        for codigo_compra, dados in compras.items():
            if compras[codigo_compra] == codigo_compra:
                print("       " + f"Código da Compra: {codigo_compra}.")
                print("       " + f"Nome do Produto: {dados['nome_produto']}.")
                print("       " + f"Preço Unitário: {dados['preco_unitario']}.")
                print("       " + f"Preço Total da Compra: {dados['preco_compra']}.")
                print("       " + f"Quantidade: {dados['qtd_produto']}.")
                print("       " + f"Tempo de Entrega: {dados['tempo_entrega']}.")
                print()
                print()
                encontrado = True


def alterar_compra():

    compras = ler_arquivo(arquivo_compras)

    while True:

        codigo_compra = input("Digite o código da compra: ")

        if not codigo_compra in compras:
            print("Compra não encontrada.")
            return
        
        print("1 - Atualizar Nome do Produto Comprado.")
        print("2 - Atualizar Quantidade Comprada.")
        print("3 - Atualizar Tempo de Entrega.")
        print("4 - Atualizar Valor Total da Compra")
        print("5 - Atualizar CNPJ do Fornecedor.")

        escolha_update_compra = int(input("Digite sua escolha: "))

        match escolha_update_compra:
            case 1:
                nome_produto = input(f"Digite o nome do produto comprado: ")
                compras[codigo_compra]['nome_produto'] = nome_produto
                escrever_arquivo(arquivo_compras, compras)
            case 2:
                qtd_produto = int(input(f"Digite quantas unidades do produto foram compradas: "))
                compras[codigo_compra]['qtd_produto'] = qtd_produto
                escrever_arquivo(arquivo_compras, compras)
            case 3:
                tempo_entrega = float(input("Digite o tempo de entrega em DIAS: "))
                compras[codigo_compra]['tempo_entrega'] = tempo_entrega
                escrever_arquivo(arquivo_compras, compras)
            case 4:
                preco_compra = float(input("Digite o valor total da compra: "))
                preco_unitario = preco_compra // qtd_produto 
                compras[codigo_compra]['preco_compra'] = preco_compra
                compras[codigo_compra]['preco_unitario'] = preco_unitario
                escrever_arquivo(arquivo_compras, compras)
            case 5:
                cnpj_fornecedor_compra = input("Digite o CNPJ do fornecedor que a compra foi feita: ")
                if not re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", cnpj_fornecedor_compra):
                    print("CNPJ Inválido!")
                    sleep(1)
                    break
                else:    
                    compras[codigo_compra]['cnpj_fornecedor_compra'] = cnpj_fornecedor_compra
                    escrever_arquivo(arquivo_compras, compras)
            case _:
                print("Compra Inválida!")
                return
            
        print("Compra atualizada com sucesso!")


def deletar_compra():

    compras = ler_arquivo(arquivo_compras)

    while True:

        codigo_compra = input("Digite o código da compra: ")
        validar_codigo(codigo_compra, compras)

        if codigo_compra in compras:
            del compras[codigo_compra]
            escrever_arquivo(arquivo_compras, compras)
            print("Compra deletada com sucesso!")
            break
        else:
            print("Compra não encontrada!")