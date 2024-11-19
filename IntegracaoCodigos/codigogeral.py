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



def criar_produto():

    while True:

        os.system('cls')

        codigo_produto = input("Digite o código do produto: ")
        
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
def listar_produto():

    if not produtos:
        print("Nenhum produto encontrado!")
    else:
        for codigo_produto, dados in produtos.items():
            print(f"Código: {codigo_produto}")
            print(f"  Nome: {dados['nome']}")

        
#Atualizar Dados de Produtos:
def atualizar_produto():

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
def deletar_produto():
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
                criar_produto()
            case 2:
                listar_produto()
            case 3:
                atualizar_produto()
            case 4:
                deletar_produto()
            case 5:
                menu_principal()
            case 6:
                print("Encerrando Sistema...")
                sleep(2)
                os.system('cls')
                break
            case _:
                print("Opção Inválida!")
                return



#--------------------------------------------------------------------------------------#



estoque = ler_arquivo_estoque(arquivo_estoque)
#PARTE DE ESTOQUES:
#Criar Produtos:

def cadastro_dias_estoque():

    while True:

        os.system('cls')

        codigo_produto = input("Digite o código do produto no estoque: ")

        if not re.match(r"^P\d{3}$", codigo_produto):
            print("Código Inválido!")
            sleep(2)
            return
        
        if not codigo_produto in produtos:
            print("Produto não encontrado.")
            return
        
        print(f"Vamos adicionar informações do produto {codigo_produto}!")

        dias_parado = int(input("Digite o número de dias que o produto está parado no estoque: "))

        if dias_parado < 0 or dias_parado % 2 != 1:
            print("Valor Inválido!")
            return
        
        estoque_minimo = float(input("Digite a quantidade minima desse produto no estoque: "))

        if estoque_minimo < 0:
            print("Valor Inválido!")
            return
        
        estoque_maximo = float(input("Digite a quantidade máxima desse produto no estoque: "))

        if estoque_maximo < 0:
            print("Valor Inválido!")
            return

        consumo_mensal = float(input("Digite o consumo mensal: "))

        if consumo_mensal < 0:
            print("Valor Inválido!")
            return
        
        estoque_seguranca = float(input("Digite o estoque de segurança: "))

        if estoque_seguranca < 0:
            print("Valor Inválido!")
            return

        produtos[codigo_produto] = {
            'dias_parado': dias_parado,
            'estoque_minimo': estoque_minimo,
            'estoque_maximo': estoque_maximo,
            'consumo_mensal': consumo_mensal,
            'estoque_seguranca': estoque_seguranca
    }
        
        carregar_arquivo_produto(arquivo_produto, produtos)
        print(f"Produto {codigo_produto} cadastrado com sucesso!")
        sleep(2)
        break


def lista_provisao_100():
    
    if not produtos:
        print("Nenhum produto encontrado!")
    else:
        for codigo_produto, dias_parado in produtos.items():
            if dias_parado > 180:
                print(f"Código: {codigo_produto}")
                print(f"Dias Parado: {dias_parado} dias")


def atualizar_estoque():

    codigo_produto = input("Digite o código do produto: ")

    if not codigo_produto in produtos:
        print("Produto não encontrado.")
        return
    
    print("1 - Atualizar Dias Parado.")
    print("2 - Atualizar Estoque Minimo.")
    print("3 - Atualizar Estoque Máximo.")
    print("4 - Atualizar Consumo Mensal.")
    print("5 - Atualizar Estoque de Segurança.")

    escolha_update_estoque = int(input("Digite sua escolha: "))

    match escolha_update_estoque:
        case 1:
            dias_parado = int(input("Digite o número de dias que o produto está parado no estoque: "))
            produtos[codigo_produto]['dias_parado'] = dias_parado
            carregar_arquivo_produto(arquivo_produto, produtos)
        case 2:
            estoque_minimo = float(input("Digite a quantidade minima desse produto no estoque: "))
            produtos[codigo_produto]['estoque_minimo'] = estoque_minimo
            carregar_arquivo_produto(arquivo_produto, produtos)
        case 3:
            estoque_maximo = float(input("Digite a quantidade máxima desse produto no estoque: "))
            produtos[codigo_produto]['estoque_maximo'] = estoque_maximo
            carregar_arquivo_produto(arquivo_produto, produtos)
        case 4:
            consumo_mensal = float(input("Digite o consumo mensal: "))
            produtos[codigo_produto]['consumo_mensal'] = consumo_mensal
            carregar_arquivo_produto(arquivo_produto, produtos)
        case 5:
            estoque_seguranca = float(input("Digite o estoque de segurança: "))
            produtos[codigo_produto]['estoque_seguranca'] = estoque_seguranca
            carregar_arquivo_produto(arquivo_produto, produtos)
        case _:
            print("Produto Inválido!")
            return
  
    print("Produto atualizado com sucesso!")


def deletar_provisao_100():

    codigo_produto = input("Digite o código do produto: ")

    if codigo_produto in produtos and produtos['dias_parado'] > 180:
        del produtos[codigo_produto]
        carregar_arquivo_produto(arquivo_produto, produtos)
        print("Produto deletado com sucesso!")
    else:
        print("Produto não encontrado!")

def menu_est():

    while True:

        menu_estoque()

        opcao_estoque = int(input("Digite sua escolha: "))

        match opcao_estoque:
            case 1:
                cadastro_dias_estoque()
            case 2:
                lista_provisao_100()
            case 3:
                atualizar_estoque()
            case 4:
                deletar_provisao_100()
            case 5:
                menu_principal()
            case 6:
                print("Encerrando Sistema...")
                sleep(2)
                os.system('cls')
                break
            case _:
                print("Opção Inválida!")
                return


menu_est()