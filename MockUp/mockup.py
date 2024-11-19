#MockUp feito para o sistema da EnginStock.

import os
from time import sleep

class cor:
    NEGRITO = '\033[1m'
    AZUL = '\033[44m'
    RESET = "\033[0m"


#MENU BOAS-VINDAS:
def menu_boas_vindas():

    os.system('cls')
    print()
    print()
    print("|" + " " + "=" * 32 + " " + "|")
    print("|" + " " + '-' * 32 + " " + "|")
    print("|" + " " + '\033[1;30;44mBEM VINDO AO SISTEMA ENGINSTOCK!\033[m' + " " * 1 + "|")
    print("|" + " " + '-' * 32 + " " + "|")
    print("|" + " " + "=" * 32 + " " + "|")
    print()
    print()


menu_boas_vindas()

#--------------------------------------------------------------------------#

#MENU INICIAL:
def menu_principal():

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

#1: Menu Produtos:
def menu_produtos():

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

#2: Menu Estoque:
def menu_estoque(): 

    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + cor.AZUL + "SISTEMA ENGINSTOCK:" + cor.RESET + " " * 42 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + "Área de Estoque:" + cor.RESET + " " * 45 + "|")
    print("|" + " " + " " * 61 + "|")
    print("|" + " " + "2.1. Cadastro Dias em Estoque." + " " * 31 + "|")
    print("|" + " " + "2.2. Listar Produtos com Provisão 100%." + " " * 22 + "|")
    print("|" + " " + "2.3. Alterar informações de estoque." + " " * 25 + "|")
    print("|" + " " + "2.4. Deletar Produtos com Provisão 100%." + " " * 21 + "|")
    print("|" + " " + "2.5. Voltar." + " " * 49 + "|")
    print("|" + " " + "2.6. Encerrar Sistema." + " " * 39 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print()


menu_estoque()

#--------------------------------------------------------------------------#

#3: Menu Compras:
def menu_compras():

    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + cor.AZUL + "SISTEMA ENGINSTOCK:" + cor.RESET + " " * 42 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + "Área de Compras:" + cor.RESET + " " * 45 + "|")
    print("|" + " " + " " * 61 + "|")
    print("|" + " " + "3.1. Cadastrar Compra." + " " * 39 + "|")
    print("|" + " " + "3.2. Listar Histórico Compras." + " " * 31 + "|")
    print("|" + " " + "3.3. Atualizar Compra." + " " * 39 + "|")
    print("|" + " " + "3.4. Deletar Compra." + " " * 41 + "|")
    print("|" + " " + "3.5. Voltar." + " " * 49 + "|")
    print("|" + " " + "3.6. Encerrar Sistema." + " " * 39 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print()


menu_compras()

#--------------------------------------------------------------------------#

#4: Menu Fornecedores:
def menu_fornecedores():

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

#5: Menu Clientes:
def menu_clientes():

    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + cor.AZUL + "SISTEMA ENGINSTOCK:" + cor.RESET + " " * 42 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + cor.NEGRITO + "Área de Clientes:" + cor.RESET + " " * 44 + "|")
    print("|" + " " + " " * 61 + "|")
    print("|" + " " + "5.1. Cadastrar Clientes." + " " * 37 + "|")
    print("|" + " " + "5.2. Listar Clientes." + " " * 40 + "|")
    print("|" + " " + "5.3. Alterar Dados de Clientes." + " " * 30 + "|")
    print("|" + " " + "5.4. Deletar Cliente." + " " * 40 + "|")
    print("|" + " " + "5.5. Voltar." + " " * 49 + "|")
    print("|" + " " + "5.6. Encerrar Sistema." + " " * 39 + "|")
    print("|" + " " + '-' * 60 + " " + "|")
    print("|" + " " + "=" * 60 + " " + "|")
    print()


menu_clientes()

#--------------------------------------------------------------------------#

#ENCERRAR SISTEMA:
def encerrarsistema():

    os.system('cls')
    print(cor.NEGRITO + cor.AZUL + "OBRIGADO POR ESCOLHER A ENGINSTOCK!" + cor.RESET)
    print(cor.NEGRITO + cor.AZUL + '\033[1;30mENCERRANDO SISTEMA...\033[m')
    sleep(2.5)


encerrarsistema()