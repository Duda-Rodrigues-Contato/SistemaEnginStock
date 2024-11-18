#Primeira área do menu principal:

#1.1. Cadastrar Produto. (create_product)
#1.2. Listar Produtos Cadastrados. (list_product)
#1.3. Alterar Dados de Produto. (update_product)
#1.4. Deletar Produto. (delete_product)
#1.5. Voltar.
#1.6. Encerrar Sistema.

import json
import os
from time import sleep
import re
from datetime import datetime
from menus.menus import menu_produtos, menu_principal, encerrarsistema

produtos_json = os.path.join(os.path.dirname(__file__), "produtos.json") 
dados_produtos = []
produtos = {}
#Função para verificar se o arquivo existe:
def verificar_arquivo():
    if not os.path.exists(produtos_json, dados_produtos):
        with open(produtos_json, 'w') as f:
            f = json.dump(dados_produtos, f, indent=4)

#Função para carregar dados JSON:
def carregar_dados(produtos_json):
    with open(produtos_json, 'r') as f:
        return json.load(f)

#Função para salvar dados JSON:
def salvar_dados(produtos_json, dados_produtos):
    with open(produtos_json, 'w') as f:
        f = json.dump(dados_produtos, f, indent=4)

salvar_dados(produtos_json, dados_produtos)

#Inicialização dos dados:
produtos = carregar_dados(produtos_json)
dados_produtos = []
#def validar_codigo_produto(codigo_produto): 
#   return re.match(r"^\d{3}$", codigo_produto) 
# ^Inicia uma string
#OBS: o valor procurado tem 3 digitos

def validar_cnpj(cnpj):
    return re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", cnpj)
#CNPJ's: "XX.XXX.XXX/0001-XX"

def create_product():

    carregar_dados(produtos_json)

    produtos = carregar_dados(produtos_json)

    codigo_produto_str = input("Digite o código do produto: ")
    codigo_produto_int = int(codigo_produto_str)

    if not len(codigo_produto_str) == 3:
    #if not re(r"\d{3}$").match(codigo_produto): #validar_codigo_produto(codigo_produto):
        
        print("Código Inválido!")
        #print("O código deve começar por 'P' seguido por 3 caracteres.")
        print("O código deve ter três caracteres.")
    
    for produto in produtos:
        if produto['codigo_produto_str'] == codigo_produto_str:
            print("Produto já Cadastrado!")
            print("Retornando ao menu principal...")
            sleep(2)
            menu_principal()

    #if any (produtos[codigo_produto] == codigo_produto_atualizado for produtos in produtos_json):
    #    print("Produto já Cadastrado!")
    #    print("Retornando ao menu principal...")
    #    sleep(2)
    #    menu_principal()
    
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    categoria = input("Digite a categoria em que o produto se encaixa: ")
    fornecedor = input("Digite o CNPJ do fornecedor que o produto foi comprado: ")

    if not validar_cnpj(fornecedor):
        print("CNPJ inválido!")
        print("Deve seguir o seguinte padrão: XX.XXX.XXX/YYYY-ZZ")
        return 
    
    quantidade = int(input("Digite a quantidade total do produto: "))
    validade = input("Digite a data de validade do produto (caso necessário): ")
    preco = float(input("Digite o preço unitário do produto: "))

    produtos = {
        "codigo_produto": codigo_produto_int,
        "nome": nome,
        "descricao": descricao,
        "categoria": categoria,
        "fornecedor": fornecedor,
        "quantidade": quantidade, 
        "validade": validade, 
        "preco": preco
    }

    dados_produtos.append(produtos)

    # Salvar os dados atualizados
    with open(produtos_json, 'w') as f:
        json.dump(dados_produtos, f, indent=4)
    #salvar_dados(produtos_json, produtos)
    print("Produtos cadastrados com sucesso!")


def list_product():

    carregar_dados(produtos_json)
    
    #if os.path.exists(produtos_json) and os.path.getsize(produtos_json) > 0:
     #   with open(produtos_json, "r") as f:
      #      return json.load(f)
    
    if len(produtos_json) > 0 :
        #for produtos in produtos_json:
        for produtos in produtos_json:
            print(f"Código: {produtos["codigo_produto_int"]}")
            print(f"Nome: {produtos['nome']}")
    else:
        print("Nenhum produto cadastrado.")
    

def buscar_produto(codigo_produto):

    carregar_dados() #Leitura ('r')
    
    encontrado = False

    for codigo_produto in produtos:
        if produtos['codigo_produto'] == codigo_produto:
            print(f"NOME: {produtos['nome']}, CÓDIGO: {produtos['codigo']}")
            encontrado = True
    if not encontrado:
        print("Nenhum produto cadastrado.")

        
def update_product():

    codigo = input("Digite o código do produto (formato P000): ")

    if not codigo in produtos:
        print("Produto não encontrado.")
        print("Retornando ao menu principal...")
        sleep(2)
        menu_principal()
    
    print("1 - Atualizar NOME.")
    print("2 - Atualizar DESCRIÇÃO.")
    print("3 - Atualizar CATEGORIA.")
    print("4 - Atualizar QUANTIDADE.")
    print("5 - Atualizar CNPJ DO FORNECEDOR.")
    print("6 - Atualizar PREÇO UNITÁRIO.")
    print("7 - Atualizar DATA DE VALIDADE.")

    escolha_update = int(input("Digite a opção que você quer atualizar (somente o número): "))
    
    match escolha_update:
        case 1:

            nome = input("Digite o nome do produto: ")
            produtos[codigo]["nome"] = nome

            print("1 - Continuar Atualizando.")
            print("2 - Encerrar Sistema.")

            escolha_retornar = int(input("Digite sua escolha: "))

            match escolha_retornar:

                case 1:
                    return update_product()
                
                case 2:

                    print("Encerrando Sistema...")
                    sleep(2.5)
                    #Lembrar de colocar o break quando tiver no loop
        
        case 2:

            descricao = input("Digite a descrição do produto: ")
            produtos[codigo]["descricao"] = descricao

            print("1 - Continuar Atualizando.")
            print("2 - Encerrar Sistema.")

            escolha_retornar = int(input("Digite sua escolha: "))

            match escolha_retornar:

                case 1:
                    return update_product()
                
                case 2:

                    print("Encerrando Sistema...")
                    sleep(2.5)
                    #Lembrar de colocar o break quando tiver no loop
        
        case 3:

            categoria = input("Digite a categoria em que o produto se encaixa: ")
            produtos[codigo]["categoria"] = categoria

            print("1 - Continuar Atualizando.")
            print("2 - Encerrar Sistema.")

            escolha_retornar = int(input("Digite sua escolha: "))

            match escolha_retornar:

                case 1:
                    return update_product()
                
                case 2:

                    print("Encerrando Sistema...")
                    sleep(2.5)
                    #Lembrar de colocar o break quando tiver no loop

        case 4:

            quantidade = int(input("Digite a quantidade total do produto: "))
            produtos[codigo]["quantidade"] = int(quantidade)

            print("1 - Continuar Atualizando.")
            print("2 - Encerrar Sistema.")

            escolha_retornar = int(input("Digite sua escolha: "))

            match escolha_retornar:

                case 1:
                    return update_product()
                
                case 2:

                    print("Encerrando Sistema...")
                    sleep(2.5)
                    #Lembrar de colocar o break quando tiver no loop

        case 5:

            fornecedor = input("Digite o CNPJ do fornecedor que o produto foi comprado: ")
            produtos[codigo]["fornecedor_preferencial"] = fornecedor

            print("1 - Continuar Atualizando.")
            print("2 - Encerrar Sistema.")

            escolha_retornar = int(input("Digite sua escolha: "))

            match escolha_retornar:

                case 1:
                    return update_product()
                
                case 2:

                    print("Encerrando Sistema...")
                    sleep(2.5)
                    #Lembrar de colocar o break quando tiver no loop
        
        case 6:

            preco = float(input("Digite o preço unitário do produto: "))
            produtos[codigo]["preco_atual"] = float(preco)

            print("1 - Continuar Atualizando.")
            print("2 - Encerrar Sistema.")

            escolha_retornar = int(input("Digite sua escolha: "))

            match escolha_retornar:

                case 1:
                    return update_product()
                
                case 2:

                    print("Encerrando Sistema...")
                    sleep(2.5)
                    #Lembrar de colocar o break quando tiver no loop

        case 7:

            validade = input("Digite a data de validade do produto (caso necessário): ")
            produtos[codigo]["validade"] = validade

            print("1 - Continuar Atualizando.")
            print("2 - Encerrar Sistema.")

            escolha_retornar = int(input("Digite sua escolha: "))

            match escolha_retornar:

                case 1:
                    return update_product()
                
                case 2:

                    print("Encerrando Sistema...")
                    sleep(2.5)
                    #Lembrar de colocar o break quando tiver no loop
        
        case _:

            print("Opção Inválida!")

            print("1 - Continuar Atualizando.")
            print("2 - Encerrar Sistema.")

            escolha_retornar = int(input("Digite sua escolha: "))

            match escolha_retornar:

                case 1:
                    return update_product()
                
                case 2:

                    print("Encerrando Sistema...")
                    sleep(2.5)
                    #Lembrar de colocar o break quando tiver no loop
            
    

    salvar_dados(produtos_json, produtos)
    print("Produto atualizado com sucesso!")


def delete_product():

    codigo = input("Digite o código do produto (formato P000): ")

    if codigo in produtos: 
        del produtos[codigo]
        salvar_dados(produtos_json, produtos)
        print("Produto deletado com sucesso!")
    else: 
        print("Produto não encontrado!")

def main():

    while True:

        menu_produtos()

        opcao_produtos = int(input("Digite sua escolha: "))

        match opcao_produtos:

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

                encerrarsistema()
                break

            case _:

                print("Opção Inválida!")
                menu_produtos()

main()