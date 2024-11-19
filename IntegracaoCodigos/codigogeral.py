import json
import os
import re
from time import sleep
from menus.menus import *
import sys

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
def ler_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}



#--------------------------------------------------------------------------------------#



#Abrir arquivo json para ESCRITA:
def carregar_arquivo(arquivo, dados):
    try:
        with open(arquivo, 'w') as f:
            json.dump(dados, f, indent=4)
    except Exception as e:
        print(f"Erro ao salvar fdados no arquivo: {e}.")


        
#--------------------------------------------------------------------------------------#

produtos = ler_arquivo(arquivo_produto)
#PARTE DE PRODUTOS:
#Criar Produtos:
def criar_produto():

    while True:

        os.system('cls')

        codigo_produto = input("Digite o código do produto: ")
        
        if not re.match(r"^P\d{3}$", codigo_produto) or codigo_produto in produtos:
            print("Código Inválido!")
            sleep(1)
            os.system('cls')
            break
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
            sleep(1)
            os.system('cls')
            break

        produtos[codigo_produto] = {
            'nome': nome_produto,
            'descricao': descricao_produto,
            'categoria_produto': categoria_produto,
            'qtd_produto': qtd_produto,
            'preco_produto': preco_produto,
            'cnpj_fornecedor': cnpj_fornecedor
        } 


        #Escrever dados atualizados:
        carregar_arquivo(arquivo_produto, produtos)
        print(f"Produto {nome_produto} cadastrado com sucesso!")
        sleep(2)
        break
 

#Listar Produtos:
def listar_produto():

    if not produtos:
        print("Nenhum produto encontrado!")
    else:
        for codigo_produto, dados in produtos.items():
            print("-" * 25)
            print(f"Código: {codigo_produto}")
            print(f"Nome: {dados['nome']}")

        
#Atualizar Dados de Produtos:
def atualizar_produto():

    while True:

        codigo_produto = input("Digite o código do produto: ")

        if not re.match(r"^P\d{3}$", codigo_produto) or not codigo_produto in produtos:
            print("Código Inválido!")
            sleep(1)
            os.system('cls')
            break
        else:
            print("Código Válido!")
            sleep(2)
        
        print("1 - Atualizar Nome.")
        print("2 - Atualizar Descrição.")
        print("3 - Atualizar Categoria.")
        print("4 - Atualizar Quantidade em Estoque.")
        print("5 - Atualizar CNPJ do Fornecedor Preferencial.")
        print("6 - Atualizar Preço Unitário.")

        escolha_update_list = int(input("Digite sua escolha: "))

        match escolha_update_list:
            case 1:
                nome_produto = input("Digite o nome do produto: ")
                produtos[codigo_produto]['nome'] = nome_produto
                carregar_arquivo(arquivo_produto, produtos)
            case 2:
                descricao_produto = input("Digite a descrição do produto: ")
                produtos[codigo_produto]['descricao'] = descricao_produto
                carregar_arquivo(arquivo_produto, produtos)
            case 3:
                categoria_produto = input("Digite a categoria do produto: ")
                produtos[codigo_produto]['categoria_produto'] = categoria_produto
                carregar_arquivo(arquivo_produto, produtos)
            case 4:
                qtd_produto = int(input("Digite a quantidade do produto: "))
                produtos[codigo_produto]['qtd_produto'] = qtd_produto
                carregar_arquivo(arquivo_produto, produtos)
            case 5:
                cnpj_fornecedor = input("Digite o CNPJ do fornecedor preferencial para comprar o produto: ")
                if not re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", cnpj_fornecedor):
                    print("CNPJ Inválido!")
                    sleep(1)
                    break
                else:
                    produtos[codigo_produto]['cnpj_fornecedor'] = cnpj_fornecedor
                    carregar_arquivo(arquivo_produto, produtos)
            case 6:
                preco_produto = float(input("Digite o valor unitário do produto: "))
                produtos[codigo_produto]['preco_produto'] = preco_produto
                carregar_arquivo(arquivo_produto, produtos)       
            case _:
                print("Produto Inválido!")
                return
            
        print("Produto atualizado com sucesso!")


#Deletar Produtos:
def deletar_produto():

    while True:

        codigo_produto = input("Digite o código do produto: ")

        if not re.match(r"^P\d{3}$", codigo_produto):
            print("Código Inválido!")
            sleep(1)
            os.system('cls')
            break
        else:
            print("Código Válido!")
            sleep(2)

        if codigo_produto in produtos:
            del produtos[codigo_produto]
            carregar_arquivo(arquivo_produto, produtos)
            print("Produto deletado com sucesso!")
            break
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



estoque = ler_arquivo(arquivo_estoque)
produtos = ler_arquivo(arquivo_produto)
#PARTE DE ESTOQUES:
#Criar Produtos:
def cadastro_dias_estoque():
   
      while True:

        os.system('cls')

        codigo_produto = input("Digite o código do produto no estoque: ")

        if not re.match(r"^P\d{3}$", codigo_produto) or codigo_produto in produtos:
            print("Código Inválido!")
            sleep(1)
            os.system('cls')
            break
        else:
            print("Código Válido!")
            sleep(2)
            
        
        print(f"Vamos adicionar informações do produto {codigo_produto}!")

        dias_parado = int(input("Digite o número de dias que o produto está parado no estoque: "))

        if dias_parado < 0:
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

        estoque[codigo_produto] = {
            'dias_parado': dias_parado,
            'estoque_minimo': estoque_minimo,
            'estoque_maximo': estoque_maximo,
            'consumo_mensal': consumo_mensal,
            'estoque_seguranca': estoque_seguranca
    }
        
        carregar_arquivo(arquivo_estoque, estoque)
        print(f"Produto {codigo_produto} cadastrado com sucesso!")
        sleep(2)
        break


def lista_provisao_100():
    
    if not estoque:
        print("Nenhum produto encontrado!")
    else:
        for codigo_produto, dados in estoque.items():
            if dados['dias_parado'] > 180:
                print("-" * 25)
                print(f"Código: {codigo_produto}")
                print(f"Dias Parado: {dados['dias_parado']} dias")
            else:
                print("Nenhum produto com provisão 100%!")


def listar_estoque():

    if not estoque:
        print("Nenhum produto encontrada!")
    else:
        for codigo_produto, dados in estoque.items():
            print("-" * 25)
            print(f"Código: {codigo_produto}")
            print(f"Dias Parado no Estoque: {dados['dias_parado']}")
            print(f"Estoque Minimo: {dados['estoque_minimo']}")
            print(f"Estoque Máximo: {dados['estoque_maximo']}")
            print(f"Consumo Mensal: {dados['consumo_mensal']}")
            print(f"Estoque de Segurança: {dados['estoque_seguranca']}")
            


def atualizar_estoque():

    codigo_produto = input("Digite o código do produto: ")

    if not codigo_produto in estoque:
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
            estoque[codigo_produto]['dias_parado'] = dias_parado
            carregar_arquivo(arquivo_estoque, estoque)
        case 2:
            estoque_minimo = float(input("Digite a quantidade minima desse produto no estoque: "))
            estoque[codigo_produto]['estoque_minimo'] = estoque_minimo
            carregar_arquivo(arquivo_estoque, estoque)
        case 3:
            estoque_maximo = float(input("Digite a quantidade máxima desse produto no estoque: "))
            estoque[codigo_produto]['estoque_maximo'] = estoque_maximo
            carregar_arquivo(arquivo_estoque, estoque)
        case 4:
            consumo_mensal = float(input("Digite o consumo mensal: "))
            estoque[codigo_produto]['consumo_mensal'] = consumo_mensal
            carregar_arquivo(arquivo_estoque, estoque)
        case 5:
            estoque_seguranca = float(input("Digite o estoque de segurança: "))
            estoque[codigo_produto]['estoque_seguranca'] = estoque_seguranca
            carregar_arquivo(arquivo_estoque, estoque)
        case _:
            print("Produto Inválido!")
            return
  
    print("Produto atualizado com sucesso!")


def deletar_estoque():

    while True:

        codigo_produto = input("Digite o código do produto: ")

        if not re.match(r"^P\d{3}$", codigo_produto):
            print("Código Inválido!")
            sleep(1)
            os.system('cls')
            break
        else:
            print("Código Válido!")
            sleep(2)


        if codigo_produto in estoque:
            del estoque[codigo_produto]
            carregar_arquivo(arquivo_estoque, estoque)
            print("Produto deletado com sucesso!")
            break
        else:
            print("Produto não encontrado!")


def deletar_provisao_100():

    while True:

        codigo_produto = input("Digite o código do produto: ")

        if not re.match(r"^P\d{3}$", codigo_produto):
            print("Código Inválido!")
            sleep(1)
            os.system('cls')
            break
        else:
            print("Código Válido!")
            sleep(2)
            
        if not codigo_produto in estoque:  
            print("Nenhum produto encontrado!")
        else:
            for codigo_produto, dados in estoque.items():
                if dados['dias_parado'] > 180:
                    del estoque[codigo_produto]
                    carregar_arquivo(arquivo_estoque, estoque)
                    print("Produto deletado com sucesso!")
                    break
                else:
                    print("Produto não tem provisão 100%!")

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
                listar_estoque()
            case 4:
                atualizar_estoque()
            case 5:
                deletar_provisao_100()
            case 6:
                deletar_estoque()
            case 7:
                menu_principal()
            case 8:
                print("Encerrando Sistema...")
                sleep(2)
                os.system('cls')
                break
            case _:
                print("Opção Inválida!")
                return



#--------------------------------------------------------------------------------------#



compras = ler_arquivo(arquivo_compra)
#PARTE DE COMPRAS:
#Criar Produtos:
def cadastrar_compra():

    while True:

        os.system('cls')

        codigo_compra = input("Digite o código da compra: ")

        if not re.match(r"^C\d{3}$", codigo_compra) or codigo_compra in compras:
            print("Código Inválido!")
            sleep(1)
            os.system('cls')
            break
        else:
            print("Código Válido!")
            sleep(2)

        nome_produto = input("Digite o nome do produto comprado: ")
        qtd_produto = int(input("Digite quantas unidades do produto foram compradas: "))
        tempo_entrega = float(input("Digite o tempo de entrega em DIAS: "))
        preco_compra = float(input("Digite o valor total da compra: "))
        cnpj_fornecedor_compra = input("Digite o CNPJ do fornecedor que a compra foi feita: ")

        if not re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", cnpj_fornecedor_compra):
            print("CNPJ Inválido!")
            sleep(1)
            os.system('cls')
            break

        preco_unitario = preco_compra // qtd_produto 

        compras[codigo_compra] = {
            'nome_produto': nome_produto,
            'qtd_produto': qtd_produto,
            'tempo_entrega': tempo_entrega,
            'preco_compra': preco_compra,
            'preco_unitario': preco_unitario,
            'cnpj_fornecedor_compra': cnpj_fornecedor_compra
        }

        carregar_arquivo(arquivo_compra, compras)
        print(f"Produto {codigo_compra} cadastrado com sucesso!")
        sleep(2)
        break


#Listar Histórico de Compras:
def listar_compras():

    if not compras:
        print("Nenhuma compra encontrada!")
    else:
        for codigo_compra, dados in compras.items():
            print("-" * 25)
            print(f"Código: {codigo_compra}")
            print(f"Nome: {dados['nome_produto']}")
            print(f"Preço Unitário: {dados['preco_unitario']}")
            print(f"Preço Total: {dados['preco_compra']}")
            print(f"Quantidade: {dados['qtd_produto']}")
            print(f"Tempo de Entrega: {dados['tempo_entrega']}")
            

#Alterar Compra:
def alterar_compra():

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
                produtos[codigo_compra]['nome_produto'] = nome_produto
                carregar_arquivo(arquivo_compra, compras)
            case 2:
                qtd_produto = int(input(f"Digite quantas unidades do produto foram compradas: "))
                produtos[codigo_compra]['qtd_produto'] = qtd_produto
                carregar_arquivo(arquivo_compra, compras)
            case 3:
                tempo_entrega = float(input("Digite o tempo de entrega em DIAS: "))
                produtos[codigo_compra]['tempo_entrega'] = tempo_entrega
                carregar_arquivo(arquivo_compra, compras)
            case 4:
                preco_compra = float(input("Digite o valor total da compra: "))
                preco_unitario = preco_compra // qtd_produto 
                produtos[codigo_compra]['preco_compra'] = preco_compra
                produtos[codigo_compra]['preco_unitario'] = preco_unitario
                carregar_arquivo(arquivo_compra, compras)
            case 5:
                cnpj_fornecedor_compra = input("Digite o CNPJ do fornecedor que a compra foi feita: ")
                if not re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", cnpj_fornecedor_compra):
                    print("CNPJ Inválido!")
                    sleep(1)
                    break
                else:    
                    produtos[codigo_compra]['cnpj_fornecedor_compra'] = cnpj_fornecedor_compra
                    carregar_arquivo(arquivo_compra, compras)  
            case _:
                print("Compra Inválida!")
                return
            
        print("Compra atualizada com sucesso!")


#Deletar Compra:
def deletar_compra():

    while True:

        codigo_compra = input("Digite o código da compra: ")

        if not re.match(r"^C\d{3}$", codigo_compra):
            print("Código Inválido!")
            sleep(1)
            os.system('cls')
            break
        else:
            print("Código Válido!")
            sleep(2)

        if codigo_compra in compras:
            del compras[codigo_compra]
            carregar_arquivo(arquivo_compra, compras)  
            print("Compra deletada com sucesso!")
            break
        else:
            print("Compra não encontrada!")


def menu_com():

    while True:

        menu_compras()

        opcao_compras = int(input("Digite sua escolha: "))

        match opcao_compras:
            case 1:
                cadastrar_compra()
            case 2:
                listar_compras()
            case 3:
                alterar_compra()
            case 4:
                deletar_compra()
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



fornecedores = ler_arquivo(arquivo_fornecedores)
#PARTE DE FORNCEDORES:
#Criar Fornecedor:
def criar_fornecedor():

    while True:

        os.system('cls')

        codigo_fornecedor = input("Digite o código do fornecedor: ")

        if not re.match(r"^F\d{3}$", codigo_fornecedor) or codigo_fornecedor in fornecedores:
            print("Código Inválido!")
            sleep(1)
            os.system('cls')
            break
        else:
            print("Código Válido!")
            sleep(2)
        

        nome_fornecedor =  input("Digite o nome do fornecedor: ")
        cnpj_area_fornecedor = input("Digite o CNPJ do fornecedor que irá cadastrar: ")
        
        if not re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", cnpj_area_fornecedor):
            print("CNPJ Inválido!")
            sleep(1)
            os.system('cls')
            break

        tempo_de_entrega = int(input("Digite o tempo de entrega dos produtos do fornecedor em DIAS: "))


        fornecedores[codigo_fornecedor] = {
            'nome_fornecedor': nome_fornecedor,
            'cnpj_area_fornecedor': cnpj_area_fornecedor,
            'tempo_de_entrega': tempo_de_entrega
        }


        #Escrever dados atualizados:
        carregar_arquivo(arquivo_fornecedores, fornecedores)
        print(f"Produto {codigo_fornecedor} cadastrado com sucesso!")
        sleep(2)
        break


#Listar Fornecedores:
def listar_fornecedores():

    if not fornecedores:
        print("Nenhum fornecedor encontrado!")
    else:
        for codigo_fornecedor, dados in fornecedores.items():
            print("-" * 25)
            print(f"Código do Fornecedor: {codigo_fornecedor}")
            print(f"Nome do Fornecedor: {dados['nome_fornecedor']}")
            print(f"CNPJ do Fornecedor: {dados['cnpj_area_fornecedor']}")


#Atualizar Fornecedores:
def atualizar_fornecedor():

    while True:

        codigo_fornecedor = input("Digite o código do fornecedor: ")

        if not codigo_fornecedor in fornecedores:
            print("Produto não encontrado.")
            return
        
        print("1 - Atualizar Nome do Fornecedor.")
        print("2 - Atualizar Tempo de Entrega do Fornecedor.")
        print("3 - Atualizar CNPJ do Fornecedor.")

        escolha_fornecedor = int(input("Digite sua escolha: "))
        
        match escolha_fornecedor:
            case 1:
                nome_fornecedor =  input("Digite o nome do fornecedor: ")
                fornecedores[codigo_fornecedor]['nome_fornecedor'] = nome_fornecedor
                carregar_arquivo(arquivo_fornecedores, fornecedores)
            case 2:
                tempo_de_entrega = int(input("Digite o tempo de entrega dos produtos do fornecedor em DIAS:: "))
                fornecedores[codigo_fornecedor]['tempo_de_entrega'] = tempo_de_entrega
                carregar_arquivo(arquivo_fornecedores, fornecedores)
            case 3:
                cnpj_area_fornecedor = input("Digite o CNPJ do fornecedor que irá cadastrar: ")
                if not re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", cnpj_area_fornecedor):
                    print("CNPJ Inválido!")
                    sleep(1)
                    break
                else:
                    fornecedores[codigo_fornecedor]['cnpj_area_fornecedor'] = cnpj_area_fornecedor
                    carregar_arquivo(arquivo_fornecedores, fornecedores)
            case _:
                print("Fornecedor Inválido!")
                return
            
        print("Produto atualizado com sucesso!")


#Deletar Fornecedor:
def deletar_fornecedor():

    while True:

        codigo_fornecedor = input("Digite o código do fornecedor: ")

        if not re.match(r"^F\d{3}$", codigo_fornecedor):
            print("Código Inválido!")
            sleep(1)
            os.system('cls')
            break
        else:
            print("Código Válido!")
            sleep(2)

        if codigo_fornecedor in fornecedores:
            del fornecedores[codigo_fornecedor]
            carregar_arquivo(arquivo_fornecedores, fornecedores)
            print("Fornecedor deletado com sucesso!")
            break
        else:
            print("Fornecedor não encontrado!")


def menu_for():

    while True:

        menu_fornecedores()

        opcao_fornecedores = int(input("Digite sua escolha: "))

        match opcao_fornecedores:
            case 1:
                criar_fornecedor()
            case 2:
                listar_fornecedores()
            case 3:
                atualizar_fornecedor()
            case 4:
                deletar_fornecedor()
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


def validar_telefone(telefone):

    while True:

        if re.match(r"^9\.\d{4}-\d{4}$", telefone):
            print("Telefone Válido!")
            return telefone
        else:
            print("Telefone Inválido!")
            sleep(2)

    
clientes = ler_arquivo(arquivo_clientes)
#PARTE DE CLIENTES:
#Criar Cliente:
def criar_cliente():

    while True:

        os.system('cls')

        codigo_cliente = input("Digite o código do cliente: ")

        if not re.match(r"^CL\d{3}$", codigo_cliente) or codigo_cliente in clientes:
            print("Código Inválido!")
            sleep(1)
            os.system('cls')
            break
        else:
            print("Código Válido!")
            sleep(2)

        nome_cliente = input("Digite o nome do cliente que irá cadastrar: ")
        cnpj_cliente = input("Digite o CNPJ do cliente que irá cadastrar: ")

        if not re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", cnpj_cliente):
            print("CNPJ Inválido!")
            sleep(1)
            os.system('cls')
            break

        telefone_cliente = input("Digite o telefone do cliente que irá cadastrar começando com 9: ")
        validar_telefone(telefone_cliente)

        clientes[codigo_cliente] = {
            'nome_cliente': nome_cliente,
            'cnpj_cliente': cnpj_cliente,
            'telefone_cliente': telefone_cliente
        }

        #Escrever dados atualizados:
        carregar_arquivo(arquivo_clientes, clientes)
        print(f"Cliente {codigo_cliente} cadastrado com sucesso!")
        sleep(2)
        break


#Listar Clientes:
def listar_clientes():

    if not clientes:
        print("Nenhum cliente encontrado!")
    else:
        for codigo_cliente, dados in clientes.items():
            print("-" * 25)
            print(f"Código do Cliente: {codigo_cliente}")
            print(f"Nome do Cliente: {dados['nome_cliente']}")
            print(f"CNPJ do Cliente: {dados['cnpj_cliente']}")
            print(f"Telefone do Cliente: {dados['telefone_cliente']}")


#Atualizar Clientes:
def atualizar_clientes():

    while True:

        codigo_cliente = input("Digite o código do cliente: ")

        if not codigo_cliente in clientes:
            print("Cliente não encontrado.")
            return

        print("1 - Atualizar Nome do Cliente.")
        print("2 - Atualizar CNPJ do Cliente.")
        print("3 - Atualizar Telefone do Cliente.")

        escolha_cliente = int(input("Digite sua escolha: "))

        match escolha_cliente:
            case 1:
                nome_cliente = input("Digite o nome do cliente que irá cadastrar: ")
                clientes[codigo_cliente]['nome_fornecedor'] = nome_cliente
                carregar_arquivo(arquivo_clientes, clientes)
            case 2:
                cnpj_cliente = input("Digite o CNPJ do cliente que irá cadastrar: ")
                if not re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", cnpj_cliente):
                    print("CNPJ Inválido!")
                    sleep(1)
                    break
                else:
                    clientes[codigo_cliente]['cnpj_cliente'] = cnpj_cliente
                    carregar_arquivo(arquivo_clientes, clientes)
            case 3:
                telefone_cliente = input("Digite o telefone do cliente que irá cadastrar começando com 9: ")
                validar_telefone(telefone_cliente)
                clientes[codigo_cliente]['telefone_cliente'] = telefone_cliente
                carregar_arquivo(arquivo_clientes, clientes)
            case _:
                print("Fornecedor Inválido!")
                return
            
        print("Produto atualizado com sucesso!")


#Deletar Cliente:
def deletar_cliente():

    while True:

        codigo_cliente = input("Digite o código do cliente: ")

        if not re.match(r"^CL\d{3}$", codigo_cliente):
            print("Código Inválido!")
            sleep(1)
            os.system('cls')
            break
        else:
            print("Código Válido!")
            sleep(2)

        if codigo_cliente in clientes:
            del clientes[codigo_cliente]
            carregar_arquivo(arquivo_clientes, clientes)
            print("Cliente deletado com sucesso!")
            break
        else:
            print("Cliente não encontrado!")


def menu_cli():

    while True:

        menu_clientes()

        opcao_clientes = int(input("Digite sua escolha: "))

        match opcao_clientes:
            case 1:
                criar_cliente()
            case 2:
                listar_clientes()
            case 3:
                atualizar_clientes()
            case 4:
                deletar_cliente()
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



#FUNCIONAMENTO DO CÓDIGO:
def main():

    menu_boas_vindas()

    sleep(1.5)

    os.system('cls')

    menu_principal()

    escolha_menu_principal = int(input(cor.NEGRITO + "DIGITE SUA ESCOLHA: " + cor.RESET))

    match escolha_menu_principal:
        case 1:

            while True:

                menu_produtos()

                opca_produtos = int(input(cor.NEGRITO + "DIGITE SUA ESCOLHA (APENAS O ÚLTIMO NÚMERO): " + cor.RESET))

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
                        main()
                    case 6:
                        encerrarsistema()
                    case _:
                        print("Opção Inválida!")
                        return
        case 2:
            
            while True:

                menu_estoque()

                opcao_estoque = float(input(cor.NEGRITO + "DIGITE SUA ESCOLHA (APENAS O ÚLTIMO NÚMERO): " + cor.RESET))

                match opcao_estoque:
                    case 1:
                        cadastro_dias_estoque()
                    case 2:
                        lista_provisao_100()
                    case 3:
                        listar_estoque()
                    case 4:
                        atualizar_estoque()
                    case 5:
                        deletar_provisao_100()
                    case 6:
                        deletar_estoque()
                    case 7:
                        main()
                    case 8:
                        encerrarsistema()
                    case _:
                        print("Opção Inválida!")
                        return

        case 3:

            while True:

                menu_compras()

                opcao_compras = int(input(cor.NEGRITO + "DIGITE SUA ESCOLHA (APENAS O ÚLTIMO NÚMERO): " + cor.RESET))

                match opcao_compras:
                    case 1:
                        cadastrar_compra()
                    case 2:
                        listar_compras()
                    case 3:
                        alterar_compra()
                    case 4:
                        deletar_compra()
                    case 5:
                        main()
                    case 6:
                        encerrarsistema()
                    case _:
                        print("Opção Inválida!")
                        return

        case 4:
            
            while True:

                menu_fornecedores()

                opcao_fornecedores = int(input(cor.NEGRITO + "DIGITE SUA ESCOLHA (APENAS O ÚLTIMO NÚMERO): " + cor.RESET))

                match opcao_fornecedores:
                    case 1:
                        criar_fornecedor()
                    case 2:
                        listar_fornecedores()
                    case 3:
                        atualizar_fornecedor()
                    case 4:
                        deletar_fornecedor()
                    case 5:
                        main()
                    case 6:
                        encerrarsistema()
                    case _:
                        print("Opção Inválida!")
                        return
            
        case 5:
            
            while True:

                menu_clientes()

                opcao_clientes = int(input(cor.NEGRITO + "DIGITE SUA ESCOLHA (APENAS O ÚLTIMO NÚMERO): " + cor.RESET))

                match opcao_clientes:
                    case 1:
                        criar_cliente()
                    case 2:
                        listar_clientes()
                    case 3:
                        atualizar_clientes()
                    case 4:
                        deletar_cliente()
                    case 5:
                        main()
                    case 6:
                        encerrarsistema()
                    case _:
                        print("Opção Inválida!")
                        return

        case 6:
            encerrarsistema()

        case _:
            print("Opção Inválida!")
            print(cor.NEGRITO + cor.AZUL + "OBRIGADO POR ESCOLHER A ENGINSTOCK!" + cor.RESET)
            print(cor.NEGRITO + cor.AZUL + '\033[1;30mENCERRANDO SISTEMA...\033[m')
            sleep(1.5)
            sys.exit()

main()
