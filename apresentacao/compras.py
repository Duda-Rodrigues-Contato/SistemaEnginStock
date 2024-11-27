#Responsável: Duda Rodrigues

import json
import os
import re
from menus import *
from uteis import *

arquivo_compras = "SistemaEnginStock/apresentacao/DataBase/compras.json"
arquivo_existe(arquivo_compras)

def adicionar_compra(codigo_compra, nome_produto, qtd_produto, tempo_produto, preco_compra, preco_unitario, cnpj_fornecedor_compra):

    compras = ler_arquivo(arquivo_compras)

    compras[codigo_compra] = {
        'nome_produto': nome_produto,
        'qtd_produto': qtd_produto,
        'tempo_produto': tempo_produto,
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
            print()
            print()


def buscar_compra(codigo_compra, codigo_compra_buscar):

    compras = ler_arquivo(arquivo_compras)

    if not compras:
        print("NENHUMA COMPRA CADASTRADA!")