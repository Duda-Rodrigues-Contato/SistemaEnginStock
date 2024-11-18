import json
import re
from datetime import datetime

# Arquivo JSON para persistência de dados
PRODUTOS_JSON = "produtos.json"

# Funções para carregar e salvar dados JSON
def carregar_dados(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

# Inicialização dos dados
produtos = carregar_dados(PRODUTOS_JSON)

def validar_codigo_produto(codigo): 
    return re.match(r"^P\d{3}$", codigo) 

def validar_cnpj(cnpj):
    return re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", cnpj)

def cadastro_produtos(): 
    codigo = (input(" DIGITE O CÓDIGO DO PRODUTO: \n>>>"))
    if not validar_codigo_produto(codigo):
        print("Código inválido! Deve começar com 'P' seguido de três números.")
        return
    if codigo in produtos:
        print("Produto já cadastrado!")
        return
    nome = input(" DIGITE O NOME DO PRODUTO: \n>>>")
    descricao = input("DIGITE A DESCRIÇÃO DO PRODUTO: \n")
    categoria = input ( "DIGITE A CATEGORIA DO PRODUTO: \n")
    fornecedor = input ("DIGITE O CNPJ DO FORNECEDOR: \n")
    if not validar_cnpj(fornecedor):
        print("CNPJ inválido! Deve seguir o seguinte padrão: XX.XXX.XXX/YYYY-ZZ ")
        return
    quantidade = int(input("DIGITE A QUANTIDADE DE PRODUTOS: \n>>>"))
    validade = input("DIGITE A DATA DE VALIDADE DO PRODUTO: \n>>>")
    preco = float(input("DIGITE O PRECO DO PRODUTO: "))

    produtos[codigo] = {
        "nome": nome,
        "descricao": descricao,
        "categoria": categoria,
        "fornecedor": fornecedor,
        "quantidade": quantidade, 
        "validade": validade, 
        "preco": preco
}

    # Salvar os dados atualizados
    salvar_dados(PRODUTOS_JSON, produtos)
    print("\nProdutos cadastrados com sucesso!")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for codigo, dados in produtos.items():
            print(f"Código: {codigo}")
            print(f"  Nome: {dados['nome']}")

def buscar_produto(codigo):
    carregar_dados()
    
    encontrado = False

    for codigo in produtos:
        if produtos['codigo'] == codigo:
            print(f"NOME: {produtos['nome']}, CÓDIGO: {produtos['codigo']}")
            encontrado = True
    if not encontrado:
        print("😒 NENHUM PRODUTO CADASTRADO.")



def atualizar_produtos():
    codigo = input( "DIGITE O CÓDIGO DO PRODUTO(formato P000): ")
    if codigo not in produtos:
        print("Produto não encontrado.")
        return
    
    print("Deixe em branco para não alterar um campo.")
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    categoria = input("Categoria do produto: ").lower()
    quantidade = input("Quantidade em estoque: ")
    unidade = input("Unidade de medida: ")
    fornecedor = input("Fornecedor preferencial: ")
    preco = input("Preço do material: ")
    validade = input("Validade do produto: ")

    if nome:
        produtos[codigo]["nome"] = nome
    if descricao:
        produtos[codigo]["descricao"] = descricao
    if categoria:
        produtos[codigo]["categoria"] = categoria
    if quantidade:
        produtos[codigo]["quantidade"] = int(quantidade)
    if unidade:
        produtos[codigo]["unidade"] = unidade
    if fornecedor:
        produtos[codigo]["fornecedor_preferencial"] = fornecedor
    if preco:
        produtos[codigo]["preco_atual"] = float(preco)
    if validade:
        produtos[codigo]["validade"] = validade

    salvar_dados(PRODUTOS_JSON, produtos)
    print("Produto atualizado com sucesso!")

def deletar_produtos():
    codigo = input ("DIGITE O CÓDIGO DO PRODUTO QUE VOCÊ DESEJA DELETAR (formato P000): ")
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
        print("MENU PRODUTOs:")
        print("1. Cadastrar produto")
        print("2. Listar todos produtos")
        print("3. Atualizar dados do produto")
        print("4. Deletar produto")
        print("5. Voltar para o Menu Principal")
        print("6. Encerrar")
        opcao = input("Escolha uma opção: ")  

        if opcao == "1": 
            cadastro_produtos()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3": 
            atualizar_produtos()
        elif opcao == "4":
            deletar_produtos()
        elif opcao == "5":
            menu_principal()
        elif opcao == "6":
            print("Encerrando programa")
            break
        else: 
            print("Opção Invalida! Tente novamente")
            

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
            elif opcao == "6":
                print("Encerrando o sistema.")
            # Sai do loop e finaliza o programa
            else:
                print("Opção inválida. Tente novamente.")

    # Executa a função 'main' para iniciar o programa
menu_principal()