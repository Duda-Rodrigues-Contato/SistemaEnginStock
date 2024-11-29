#Responsável: Maria Luiza

import json
import os
import re
from menus import *
from uteis import *
PRODUTOS_JSON = "produtos.json"

def carregar_dados(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)


produtos = carregar_dados(PRODUTOS_JSON)

def validar_codigo_produto(codigo): 
    return re.match(r"^P\d{3}$", codigo) 

def validar_cnpj(cnpj):
    return re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", cnpj)

def cadastro_produtos(): 
    codigo = input("DIGITE O CÓDIGO DO PRODUTO (formato P000): \n>>>")
    if not validar_codigo_produto(codigo):
        print("Código inválido! Deve começar com 'P' seguido de três números.")
        return
    if codigo in produtos:
        print("Produto já cadastrado!")
        return
    nome = input("DIGITE O NOME DO PRODUTO: \n>>>")
    descricao = input("DIGITE A DESCRIÇÃO DO PRODUTO: \n")
    categoria = input("DIGITE A CATEGORIA DO PRODUTO: \n")
    fornecedor = input("DIGITE O CNPJ DO FORNECEDOR: \n")
    if not validar_cnpj(fornecedor):
        print("CNPJ inválido! Deve seguir o seguinte padrão: XX.XXX.XXX/YYYY-ZZ ")
        return
    quantidade = int(input("DIGITE A QUANTIDADE DE PRODUTOS: \n>>>"))
    validade = input("DIGITE A DATA DE VALIDADE DO PRODUTO (DD/MM/AAAA): \n>>>")
    preco = float(input("DIGITE O PREÇO DO PRODUTO: \n>>>"))

    produtos[codigo] = {
        "nome": nome,
        "descricao": descricao,
        "categoria": categoria,
        "fornecedor": fornecedor,
        "quantidade": quantidade, 
        "validade": validade, 
        "preco": preco
    }

    salvar_dados(PRODUTOS_JSON, produtos)
    print("\nProduto cadastrado com sucesso!")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for codigo, dados in produtos.items():
            print(f"Código: {codigo}")
            print(f"  Nome: {dados['nome']}")
            print("-" * 30)

def buscar_produto():
    codigo = input("DIGITE O CÓDIGO DO PRODUTO QUE DESEJA BUSCAR (formato P000): ").strip()
    if codigo in produtos:
        produto = produtos[codigo]
        print(f"\nProduto encontrado!")
        print(f"Código: {codigo}")
        print(f"Nome: {produto['nome']}")
        print(f"Descrição: {produto['descricao']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Fornecedor: {produto['fornecedor']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Validade: {produto['validade']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
    else:
        print("Produto não encontrado.")

def atualizar_produtos():
    codigo = input("DIGITE O CÓDIGO DO PRODUTO (formato P000): ")
    if codigo not in produtos:
        print("Produto não encontrado.")
        return
    
    print("Deixe em branco para não alterar um campo.")
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    categoria = input("Categoria do produto: ").lower()
    quantidade = input("Quantidade em estoque: ")
    fornecedor = input("Fornecedor (CNPJ): ")
    preco = input("Preço do produto: ")
    validade = input("Validade do produto: ")

    if nome:
        produtos[codigo]["nome"] = nome
    if descricao:
        produtos[codigo]["descricao"] = descricao
    if categoria:
        produtos[codigo]["categoria"] = categoria
    if quantidade:
        produtos[codigo]["quantidade"] = int(quantidade)
    if fornecedor:
        produtos[codigo]["fornecedor"] = fornecedor
    if preco:
        produtos[codigo]["preco"] = float(preco)
    if validade:
        produtos[codigo]["validade"] = validade

    salvar_dados(PRODUTOS_JSON, produtos)
    print("Produto atualizado com sucesso!")

def deletar_produtos():
    codigo = input("DIGITE O CÓDIGO DO PRODUTO QUE DESEJA DELETAR (formato P000): ")
    if codigo in produtos: 
        del produtos[codigo]
        salvar_dados(PRODUTOS_JSON, produtos)
        print("Produto deletado com sucesso!")
    else: 
        print("Produto não encontrado!")

def menu_produtos():
    while True:
        print("=" * 50)
        print("SISTEMA ENGINSTOCK")
        print("-" * 50)
        print("MENU PRODUTOS:")
        print("1. Cadastrar produto")
        print("2. Listar todos produtos")
        print("3. Buscar produto pelo código")
        print("4. Atualizar dados do produto")
        print("5. Deletar produto")
        print("6. Voltar para o Menu Principal")
        print("7. Encerrar")
        opcao = input("Escolha uma opção: ")  

        if opcao == "1": 
            cadastro_produtos()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            buscar_produto()
        elif opcao == "4": 
            atualizar_produtos()
        elif opcao == "5":
            deletar_produtos()
        elif opcao == "6":
            break
        elif opcao == "7":
            print("Encerrando programa")
            exit()
        else: 
            print("Opção inválida! Tente novamente.")

def menu_principal():
    while True:
        print("=" * 50)
        print("SISTEMA ENGINSTOCK")
        print("-" * 50)
        print("\nMENU PRINCIPAL:")
        print("1. Produtos")
        print("2. Fornecedor")
        print("3. Estoque")
        print("4. Compras")
        print("5. Encerrar")

        opcao = input("Escolha uma opção: ")  

        if opcao == "1":
            menu_produtos()
        elif opcao == "5":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")