import json
import os
import re
from time import sleep
from menus.menus import *

#Contadores:
cont_letra_produto = 1

#Definir arquivos de cada arquivo: 
arquivo_produto = os.path.join(os.path.dirname(__file__), "produtos.json") 
arquivo_estoque = os.path.join(os.path.dirname(__file__), "estoque.json")
arquivo_compra = os.path.join(os.path.dirname(__file__), "compras.json")
arquivo_clientes = os.path.join(os.path.dirname(__file__), "clientes.json")
arquivo_fornecedores = os.path.join(os.path.dirname(__file__), "fornecedores.json")

#Verificar se cada arquivo existe. Se não existir, ele cria (serve para escrever no arquivo também):
#Abrir arquivo json para LEITURA:
def ler_arquivo_produto(arquivo_produto): 
    #Verifica a existência do arquivo "arquivo_produto":
    if not os.path.exists(arquivo_produto):
        with open(arquivo_produto, 'r') as f:
            return json.load(f)


def ler_arquivo_estoque(arquivo_estoque):
    #Verifica a existência do arquivo "arquivo_estoque":
    if not os.path.exists(arquivo_estoque):
        with open(arquivo_estoque, 'r') as f:
            return json.load(f)


def ler_arquivo_compra(arquivo_compra):
    #Verifica a existência do arquivo "arquivo_compra":
    if not os.path.exists(arquivo_compra):
        with open(arquivo_compra, 'r') as f:
            return json.load(f)


def ler_arquivo_clientes(arquivo_clientes):
    #Verifica a existência do arquivo "arquivo_clientes":
    if not os.path.exists(arquivo_clientes):
        with open(arquivo_clientes, 'r') as f:
            return json.load(f) 


def ler_arquivo_fornecedores(arquivo_fornecedores):
    #Verifica a existência do arquivo "arquivo_fornecedores":
    if not os.path.exists(arquivo_fornecedores):
        with open(arquivo_fornecedores, 'r') as f:
            return json.load(f)



#--------------------------------------------------------------------------------------#



#Abrir arquivo json para ESCRITA:
def carregar_arquivo_produto(arquivo_produto, dados):
    #Ler o que tá no arquivo "arquivo_produto":
    with open(arquivo_produto, 'w') as f:
        json.dump(dados, f, indent=4)
        
    
def carregar_arquivo_estoque(arquivo_estoque, dados):  
    #Ler o que tá no arquivo "arquivo_produto":
    with open(arquivo_estoque, 'w') as f:
        json.dump(dados, f, indent=4)
        

def carregar_arquivo_compra(arquivo_compra, dados):
    #Ler o que tá no arquivo "arquivo_compra":
    with open(arquivo_compra, 'w') as f:
        json.dump(dados, f, indent=4)


def carregar_arquivo_clientes(arquivo_clientes, dados): 
    #Ler o que tá no arquivo "arquivo_clientes":
    with open(arquivo_clientes, 'w') as f:
        json.dump(dados, f, indent=4)


def carregar_arquivo_fornecedores(arquivo_fornecedores, dados):
    #Ler o que tá no arquivo "arquivo_fornecedores":
    with open(arquivo_fornecedores, 'w') as f:
        json.dump(dados, f, indent=4)
    


#--------------------------------------------------------------------------------------#



produtos = ler_arquivo_produto(arquivo_produto)
#PARTE DE PRODUTOS:
#Criar Produtos:
def create_product():

    while True:

        os.system('cls')

        codigo_produto = input("Digite o código do produto: ")
        #letra_codigo_produto = input("Digite a letra de identificação código: ")

        if not re.match(r"^P\d{3}$", codigo_produto):
            print("Código Inválido!")
            sleep(2)
            return
        
        else:

            print("Código Válido!")
            sleep(2)

        nome_produto = input("Digite o nome do produto: ")
        descricao_produto = input("Digite a descrição do produto: ")
        categoria_produto = input("Digite a categoria do produto: ")
        qtd_produto = int(input("Digite a quantidade do produto: "))
        preco_produto = float(input("Digite o valor unitário do produto: "))
        cnpj_fornecedor = input("Digite o CNPJ do fornecedor preferencial para comprar o produto: ")

        if not re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", cnpj_fornecedor):
            print("CNPJ Inválido!")
            sleep(2)
            return
        
        else:

            print("CNPJ Válido!")
            sleep(2)

        produtos[codigo_produto] = {
            'nome': nome_produto,
            'descricao': descricao_produto,
            'categoria_produto': categoria_produto,
            'qtd_produto': qtd_produto,
            'preco_produto': preco_produto,
            'cnpj_fornecedor': cnpj_fornecedor
        } 

        #Escrever dados atualizados:
        carregar_arquivo_produto(arquivo_produto, produtos)
        print(f"Produto {nome_produto} cadastrado com sucesso!")
        sleep(2)
        break
        

#Listar Produtos:
def list_product():

    if not produtos:
        print("Nenhum produto encontrado!")
    else:
        for codigo_produto, dados in produtos.items():
            print(f"Código: {codigo_produto}")
            print(f"  Nome: {dados['nome']}")

        
#Atualizar Dados de Produtos:
def update_list():

    codigo_produto = input("Digite o código do produto: ")

    if not codigo_produto in produtos:
        print("Produto não encontrado.")
        return
    
    print("1 - Atualizar Nome.")
    print("2 - Atualizar Descrição.")
    print("3 - Atualizar Categoria.")
    print("4 - Atualizar Quantidade em Estoque.")
    print("5 - Atualizar Fornecedor Preferencial.")
    print("6 - Atualizar Preço Unitário.")

    escolha_update_list = int(input("Digite sua escolha: "))

    match escolha_update_list:
        case 1:
            nome_produto = input("Digite o nome do produto: ")
            produtos[codigo_produto]['nome'] = nome_produto
            carregar_arquivo_produto(arquivo_produto, produtos)
        case 2:
            descricao_produto = input("Digite a descrição do produto: ")
            produtos[codigo_produto]['descricao'] = descricao_produto
            carregar_arquivo_produto(arquivo_produto, produtos)
        case 3:
            categoria_produto = input("Digite a categoria do produto: ")
            produtos[codigo_produto]['categoria_produto'] = categoria_produto
            carregar_arquivo_produto(arquivo_produto, produtos)
        case 4:
            qtd_produto = int(input("Digite a quantidade do produto: "))
            produtos[codigo_produto]['qtd_produto'] = qtd_produto
            carregar_arquivo_produto(arquivo_produto, produtos)
        case 5:
            cnpj_fornecedor = input("Digite o CNPJ do fornecedor preferencial para comprar o produto: ")
            produtos[codigo_produto]['cnpj_fornecedor'] = cnpj_fornecedor
            carregar_arquivo_produto(arquivo_produto, produtos)
        case 6:
            preco_produto = float(input("Digite o valor unitário do produto: "))
            produtos[codigo_produto]['preco_produto'] = preco_produto
            carregar_arquivo_produto(arquivo_produto, produtos)       
        case _:
            print("Produto Inválido!")
            return
        
    carregar_arquivo_produto(arquivo_produto, produtos)
    print("Produto atualizado com sucesso!")


#Deletar Produtos:
def delete_product():
    codigo_produto = input("Digite o código do produto: ")

    if codigo_produto in produtos:
        del produtos[codigo_produto]
        carregar_arquivo_produto(arquivo_produto, produtos)
        print("Produto deletado com sucesso!")
    else:
        print("Produto não encontrado!")