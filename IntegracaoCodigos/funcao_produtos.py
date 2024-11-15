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

#Função para verificar se o arquivo existe:
def verificar_arquivo():
    if not os.path.exists(produtos_json):
        with open(produtos_json, 'w') as f:
            f = json.dump([], f, indent=4)

verificar_arquivo()

#Função para carregar dados JSON:
def carregar_dados(produtos_json):
    with open(produtos_json, 'r') as f:
        f = json.load(f)

#Função para salvar dados JSON:
def salvar_dados(produtos_json):
    with open(produtos_json, 'w') as f:
        f = json.dump([], f, indent=4)

salvar_dados(produtos_json)

#Inicialização dos dados:
produtos = carregar_dados(produtos_json)

def validar_codigo_produto(codigo): 
    return re.match(r"^P\d{3}$", codigo) 
# ^Inicia uma string
#OBS: o valor procurado tem 3 digitos

def validar_cnpj(cnpj):
    return re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", cnpj)
#CNPJ's: "XX.XXX.XXX/0001-XX"

def create_product():

    carregar_dados(produtos_json)

    codigo_produto = input("Digite o código do produto: ")
    produtos = [int(codigo_produto) for codigo_produto in produtos]
    
    if not validar_codigo_produto(codigo_produto):
        
        print("Código Inválido!")
        print("O código deve começar por 'P' seguido por 3 caracteres.")

    if any (produtos["codigo_produto"] == codigo_produto for produtos in produtos_json):
        print("Produto já Cadastrado!")
        print("Retornando ao menu principal...")
        sleep(2)
        menu_principal()
    
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

    produtos = [int(codigo_produto) for codigo_produto in produtos]

    produtos[codigo_produto] == {
        "nome": nome,
        "descricao": descricao,
        "categoria": categoria,
        "fornecedor": fornecedor,
        "quantidade": quantidade, 
        "validade": validade, 
        "preco": preco
    }

    # Salvar os dados atualizados
    salvar_dados(produtos_json, produtos)
    print("Produtos cadastrados com sucesso!")


def list_product():
    carregar_dados()
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for codigo, dados in produtos.items():
            print(f"Código: {codigo}")
            print(f"Nome: {dados['nome']}")


def buscar_produto(codigo):

    carregar_dados() #Leitura ('r')
    
    encontrado = False

    for codigo in produtos:
        if produtos['codigo'] == codigo:
            print(f"NOME: {produtos['nome']}, CÓDIGO: {produtos['codigo']}")
            encontrado = True
    if not encontrado:
        print("Nenhum produto cadastrado.")


def retornar_update():

    print("1 - Continuar Atualizando.")
    print("2 - Encerrar Sistema.")
        

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

            retornar_update()

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

            retornar_update()

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

            retornar_update()

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

            retornar_update()

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

            retornar_update()

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

            retornar_update()

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

            retornar_update()

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

            retornar_update()

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