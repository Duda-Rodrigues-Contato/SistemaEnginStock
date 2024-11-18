import json
import os
import re
from time import sleep
from menus.menus import *

#Contadores:
cont_letra_produto = 1

#Definir arquivos de cada arquivo: 
arquivo_produto = "produtos.json"
arquivo_estoque = "estoque.json"
arquivo_compra = "compras.json"
arquivo_clientes = "clientes.json"
arquivo_fornecedores = "fornecedores.json"

#Verificar se cada arquivo existe. Se não existir, ele cria (serve para escrever no arquivo também):
#Abrir arquivo json para LEITURA:
def ler_arquivo_produto(arquivo_produto): 
    try: 
        with open(arquivo_produto, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def ler_arquivo_estoque(arquivo_estoque):
    try: 
        with open(arquivo_estoque, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def ler_arquivo_compra(arquivo_compra):
    try: 
        with open(arquivo_compra, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def ler_arquivo_cliente(arquivo_clientes):
    try: 
        with open(arquivo_clientes, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def ler_arquivo_fornecedores(arquivo_fornecedores):
    try: 
        with open(arquivo_fornecedores, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}



#--------------------------------------------------------------------------------------#



#Abrir arquivo json para ESCRITA:
def carregar_arquivo_produto(arquivo_produto, dados):
    try:
        with open(arquivo_produto, 'w') as f:
            json.dump(dados, f, indent=4)
    except Exception as e:
        print(f"Erro ao salvar fdados no arquivo: {e}.")


def carregar_arquivo_estoque(arquivo_estoque, dados):
    try:
        with open(arquivo_estoque, 'w') as f:
            json.dump(dados, f, indent=4)
    except Exception as e:
        print(f"Erro ao salvar fdados no arquivo: {e}.")


def carregar_arquivo_compra(arquivo_compra, dados):
    try:
        with open(arquivo_compra, 'w') as f:
            json.dump(dados, f, indent=4)
    except Exception as e:
        print(f"Erro ao salvar fdados no arquivo: {e}.")


def carregar_arquivo_cliente(arquivo_clientes, dados):
    try:
        with open(arquivo_clientes, 'w') as f:
            json.dump(dados, f, indent=4)
    except Exception as e:
        print(f"Erro ao salvar fdados no arquivo: {e}.")


def carregar_arquivo_fornecedores(arquivo_fornecedores, dados):
    try:
        with open(arquivo_fornecedores, 'w') as f:
            json.dump(dados, f, indent=4)
    except Exception as e:
        print(f"Erro ao salvar fdados no arquivo: {e}.")


        
#--------------------------------------------------------------------------------------#



produtos = ler_arquivo_produto(arquivo_produto)
#PARTE DE PRODUTOS:
#Criar Produtos:
def validar_cnpj():
    
    while True:

        cnpj_fornecedor = input("Digite o CNPJ do fornecedor preferencial para comprar o produto: ")

        if re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", cnpj_fornecedor):
        
            print("CNPJ Válido!")
            return cnpj_fornecedor
        
        else:
            print("CNPJ Inválido!")
            sleep(2)



def create_product():

    while True:

        os.system('cls')

        codigo_produto = input("Digite o código do produto: ")
        #letra_codigo_produto = input("Digite a letra de identificação código: ")
        print(type(codigo_produto))
        if not re.match(r"^P\d{3}$", codigo_produto):
            print("Código Inválido!")
            sleep(2)
            return
        
        print("Código Válido!")
        sleep(2)

        nome_produto = input("Digite o nome do produto: ")
        descricao_produto = input("Digite a descrição do produto: ")
        categoria_produto = input("Digite a categoria do produto: ")
        qtd_produto = int(input("Digite a quantidade do produto: "))
        preco_produto = float(input("Digite o valor unitário do produto: "))
        cnpj_fornecedor = validar_cnpj()

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
def update_product():

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

def menu_pro():

    while True:

        menu_produtos()

        opca_produtos = int(input("Digite sua escolha: "))

        match opca_produtos:
            case 1:
                create_product()
            case 2:
                list_product()
            case 3:
                update_product()
            case 4:
                delete_product()
            case 5:
                menu_principal()
            case 6:
                print("Encerrando Sistema...")
                sleep(2)
                break
            case _:
                print("Opção Inválida!")
                return



#--------------------------------------------------------------------------------------#



estoque = ler_arquivo_estoque(arquivo_estoque)
#PARTE DE ESTOQUES:
#Criar Produtos:

#def cadastro_dias_estoque():

    #while True: