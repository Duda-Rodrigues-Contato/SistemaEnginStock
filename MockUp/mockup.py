#MockUp feito para o sistema da EnginStock.

import os

class cor:
    NEGRITO = '\033[1m'
    AZUL = '\033[44m'
    RESET = "\033[0m"


def menu_principal():

    os.system('cls')
    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + cor.AZUL + "SISTEMA ENGINSTOCK:" + cor.RESET + " " * 42 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " +  "=" * 60 + " " + "|")
    print("|" + " " +  '-' * 60 + " " + "|")
    print("|" + " " +  cor.NEGRITO + "Menu Inicial:" + cor.RESET + " " * 48 + "|")
    print("|" + " " + " " * 61 + "|")
    print("|" + " " + "1. Área de Produtos." + " " * 41 + "|")
    print("|" + " " + "2. Área de Estoque." + " " * 42 + "|")
    print("|" + " " + "3. Área de Compras" + " " * 43 + "|")
    print("|" + " " + "4. Área de Fornecedores." + " " * 37 + "|")
    print("|" + " " + "5. Área de Clientes." + " " * 41 + "|")
    print("|" + " " + "6. Encerrar Sistema." + " " * 41 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print()


menu_principal()

#--------------------------------------------------------------------------#

def menu_produtos():

    os.system('cls')
    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + cor.AZUL + "SISTEMA ENGINSTOCK:" + cor.RESET + " " * 42 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + "Área de Produtos:" + cor.RESET + " " * 44 + "|")
    print("|" + " " + " " * 61 + "|")
    print("|" + " " + "1.1. Cadastrar Produto." + " " * 38 + "|")
    print("|" + " " + "1.2. Listar Produtos Cadastrados." + " " * 28 + "|")
    print("|" + " " + "1.3. Alterar Dados de Produto." + " " * 31 + "|")
    print("|" + " " + "1.4. Deletar Produto." + " " * 40 + "|")
    print("|" + " " + "1.5. Voltar." + " " * 49 + "|")
    print("|" + " " + "1.6. Encerrar Sistema." + " " * 39 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print()


menu_produtos()

#--------------------------------------------------------------------------#

def menu_estoque(): 

    os.system('cls')
    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + cor.AZUL + "SISTEMA ENGINSTOCK:" + cor.RESET + " " * 42 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + "Área de Estoque:" + cor.RESET + " " * 45 + "|")
    print("|" + " " + " " * 61 + "|")
    print("|" + " " + "2.1. Cadastrar Informações." + " " * 34 + "|")
    print("|" + " " + "2.2. Listar Produtos com Provisão 100%." + " " * 22 + "|")
    print("|" + " " + "2.3. Alterar Produtos Removidos por Provisão 100%." + " " * 11 + "|")
    print("|" + " " + "2.4. Deletar Produtos com Provisão 100%." + " " * 21 + "|")
    print("|" + " " + "2.5. Voltar." + " " * 49 + "|")
    print("|" + " " + "2.6. Encerrar Sistema." + " " * 39 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print()


menu_estoque()

#--------------------------------------------------------------------------#

def menu_compras():

    os.system('cls')
    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + cor.AZUL + "SISTEMA ENGINSTOCK:" + cor.RESET + " " * 42 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + "Área de Compras:" + cor.RESET + " " * 45 + "|")
    print("|" + " " + " " * 61 + "|")
    print("|" + " " + "3.1. Cadastrar Compra." + " " * 38 + "|")
    print("|" + " " + "3.2. Listar Compras." + " " * 40 + "|")
    print("|" + " " + "3.3. Atualizar Compra." + " " * 38 + "|")
    print("|" + " " + "3.4. Deletar Compra." + " " * 40 + "|")
    print("|" + " " + "3.5. Voltar." + " " * 48 + "|")
    print("|" + " " + "3.6. Encerrar Sistema." + " " * 38 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print()


menu_compras()

#--------------------------------------------------------------------------#

def menu_fornecedores():

    os.system('cls')
    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + cor.AZUL + "SISTEMA ENGINSTOCK:" + cor.RESET + " " * 42 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + "Área de Fornecedores:" + cor.RESET + " " * 40 + "|")
    print("|" + " " + " " * 61 + "|")
    print("|" + " " + "4.1. Cadastrar Fornecedores." + " " * 33 + "|")
    print("|" + " " + "4.2. Listar Fornecedores." + " " * 36 + "|")
    print("|" + " " + "4.3. Alterar Dados de Fornecedores." + " " * 26 + "|")
    print("|" + " " + "4.4. Deletar Fornecedor." + " " * 37 + "|")
    print("|" + " " + "4.5. Voltar." + " " * 49 + "|")
    print("|" + " " + "4.6. Encerrar Sistema." + " " * 39 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print()


menu_fornecedores()

#--------------------------------------------------------------------------#

def menu_clientes():

    os.system('cls')
    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + cor.AZUL + "SISTEMA ENGINSTOCK:" + cor.RESET + " " * 42 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + "Área de Fornecedores:" + cor.RESET + " " * 40 + "|")
    print("|" + " " + " " * 61 + "|")
    print("|" + " " + "5.1. Cadastrar Clientes." + " " * 33 + "|")
    print("|" + " " + "5.2. Listar Clientes." + " " * 36 + "|")
    print("|" + " " + "5.3. Alterar Dados de Clientes." + " " * 26 + "|")
    print("|" + " " + "5.4. Deletar Cliente." + " " * 37 + "|")
    print("|" + " " + "5.5. Voltar." + " " * 49 + "|")
    print("|" + " " + "5.6. Encerrar Sistema." + " " * 39 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print()


menu_clientes()