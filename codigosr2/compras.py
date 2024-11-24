#Responsável:  Duda Rodrigues
#3.1. Cadastrar Compra. - OK
#3.2. Listar Histórico Compras. - OK
#3.3. Buscar Compra Cadastrada. - OK
#3.4. Atualizar Compra. - OK
#3.5. Deletar Compra. - OK
#3.6. Voltar.
#3.7. Encerrar Sistema.

import json
import sys #para sair do sistema
from menus import *
from uteis import *

arquivo_compras = "SistemaEnginStock/codigosr2/DataBase/comprassr2.json"

compras = ler_arquivo(arquivo_compras)

def adicionar_compra(codigo_compra, nome_produto, qtd_produto, tempo_entrega, preco_compra, preco_unitario, cnpj_fornecedor_compra):

    compras = ler_arquivo(arquivo_compras)

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
            print("       " + f"Nome de Produto: {dados['nome_produto']}.")
            print("       " + f"Preço Unitário: {dados['preco_unitario']}.")
            print("       " + f"Preço Total da Compra: {dados['preco_compra']}.")
            print()
            print()
        

def buscar_compra(codigo_compra, codigo_compra_buscar):

    compras = ler_arquivo(arquivo_compras)

    #codigo_compra = input("Digite o código da compra: ")
    #validar_codigo_buscar(codigo_compra, compras)

    #for dados in compras:
    #for codigo_compra, dados in compras.items():

    if not compras:
        print("NENHUMA COMPRA CADASTRADA!")
    else:
        print(compras.get(codigo_compra, "Compra Não Encontrada!"))
        #for codigo_compra in compras:
            #buscar()
            #if compras[codigo_compra] == codigo_compra:
                
                #print("       " + f"Código da Compra: {compras[codigo_compra]}.")
                #print("       " + f"Nome de Produto: {compras['nome_produto']}.")
                #print("       " + f"Preço Unitário: {compras['preco_unitario']}.")
                #print("       " + f"Preço Total da Compra: {compras['preco_compra']}.")
                #print()
                #print()


def atualizar_compra():

    compras = ler_arquivo(arquivo_compras)

    codigo_compra = input("Digite o código da compra: ")
    validar_codigo(codigo_compra, compras)
    
    att_compra()

    escolha_update_compra = int(input("Digite sua escolha: "))

    match escolha_update_compra:
        case 1:
            nome_produto = input("DIGITE O NOVO NOME: ")
            compras[codigo_compra]['nome_produto'] = nome_produto
            escrever_arquivo(arquivo_compras, nome_produto)
        case 2:
            qtd_produto = int(input(f"DIGITE QUANTAS UNIDADES DO PRODUTO FORAM COMPRADAS: "))
            compras[codigo_compra]['qtd_produto'] = qtd_produto
            escrever_arquivo(arquivo_compras, qtd_produto)
        case 3:
            tempo_entrega = float(input("DIGITE O TEMPO DE ENTREGA EM DIAS: "))
            compras[codigo_compra]['tempo_entrega'] = tempo_entrega
            escrever_arquivo(arquivo_compras, tempo_entrega)
        case 4:
            preco_compra = float(input("DIGITE O VALOR TOTAL DA COMPRA: "))
            preco_unitario = preco_compra // qtd_produto 
            compras[codigo_compra]['preco_compra'] = preco_compra
            compras[codigo_compra]['preco_unitario'] = preco_unitario
            escrever_arquivo(arquivo_compras, preco_compra)
            escrever_arquivo(arquivo_compras, preco_unitario)
        case 5:
            cnpj_fornecedor_compra = input("DIGITE O CNPJ DO FORNECEDOR EM QUE A COMPRA FOI FEITA: ")
            compras[codigo_compra]['cnpj_fornecedor_compra'] = cnpj_fornecedor_compra
            escrever_arquivo(arquivo_compras, cnpj_fornecedor_compra)

    print("COMPRA ATUALIZADA COM SUCESSO!")


def deletar_compra(codigo_compra):

    compras = ler_arquivo(arquivo_compras)

    codigo_compra = input("Digite o código da compra: ")

    if not codigo_compra in compras:
        print(("COMPRA NÃO CADASTRADA!"))
    else:
        for codigo_compra in compras:
            if compras[codigo_compra] == codigo_compra:
                del compras[codigo_compra]
        
        escrever_arquivo(arquivo_compras, compras)
        print("COMPRA DELETADA COM SUCESSO!")

def main_compras():

    while True:
        
        compras = ler_arquivo(arquivo_compras)
        menu_compras()
        
        escolha_compras = int(input("DIGITE SUA ESCOLHA: "))

        match escolha_compras:
            case 1:

                while True:
                    codigo_compra = input("Digite o código da compra: ")
                    validar_codigo(codigo_compra, compras)
                    nome_produto = input("Digite o nome do produto comprado: ")
                    qtd_produto = int(input("Digite quantas unidades do produto foram compradas: "))
                    tempo_entrega = float(input("Digite o tempo de entrega em DIAS: "))
                    preco_compra = float(input("Digite o valor total da compra: "))
                    preco_unitario = preco_compra // qtd_produto 
                    cnpj_fornecedor_compra = input("Digite o CNPJ do fornecedor que a compra foi feita: ")
                    validar_cnpj(cnpj_fornecedor_compra)
                    adicionar_compra(codigo_compra, nome_produto, qtd_produto, tempo_entrega, preco_compra, preco_unitario, cnpj_fornecedor_compra)
                    return menu_compras()
            case 2:
                listar_compras()
                sleep(3)
            case 3:

                while True:
                    codigo_compra_buscar = input("Digite o código da compra: ")
                    validar_codigo_buscar(codigo_compra, compras)
                    print("Teste159")
                    buscar_compra(codigo_compra)
                    print("Teste161")
                    return menu_compras()
            case 4:
                atualizar_compra()
                return menu_compras()
            case 5:
                codigo_compra = input("Digite o código da compra: ")
                deletar_compra(codigo_compra)
                return menu_compras()
            case 6:
                menu_inicial()
            case 7:
                encerrar_sistema()
            case _:
                print("VALOR INVÁLIDO!")
                menu_compras()


main_compras()