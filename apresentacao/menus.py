import os

#CORES:
# '\033[    \033[m' inicio e parada
#1 - Bold
#30 - Texto Branco
#44 - Fundo Azul

def menu_boas_vindas():

    os.system('cls')
    print()
    print()
    print("  " + "|" + " " + "=" * 34 + " " + "|")
    print("  " + "|" + " " + '-' * 34 + " " + "|")
    print("  " + "|" + "  " + '\033[1;30;44mBEM VINDO AO SISTEMA ENGINSTOCK!\033[m' + " " * 2 + "|")
    print("  " + "|" + " " + '-' * 34 + " " + "|")
    print("  " + "|" + " " + "=" * 34 + " " + "|")
    print()
    print()


def menu_inicial():

    print()
    print()
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + "  " * 10 + '\033[1;30;44mSISTEMA ENGINSTOCK:\033[m' + " " * 23 + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " +  "=" * 60 + " " + "|")
    print("  " + "|" + " " +  '-' * 60 + " " + "|")
    print("  " + "|" + " " * 62 + "|")
    print("  " + "|" + " " * 23 + '\033[1mMenu Inicial:\033[m' + " " * 26 + "|")
    print("  " + "|" + " " * 20 + " " * 42 + "|")
    print("  " + "|" + " " * 20 + "1. Área de Produtos." + " " * 22 + "|")
    print("  " + "|" + " " * 20 + "2. Área de Estoque." + " " * 23 + "|")
    print("  " + "|" + " " * 20 + "3. Área de Compras" + " " * 24 + "|")
    print("  " + "|" + " " * 20 + "4. Área de Fornecedores." + " " * 18 + "|")
    print("  " + "|" + " " * 20 + "5. Área de Clientes." + " " * 22 + "|")
    print("  " + "|" + " " * 20 + "6. Encerrar Sistema." + " " * 22 + "|")
    print("  " + "|" + " " * 62 + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print()
    print()


def menu_produtos():

    os.system('cls')
    print()
    print()
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + "  " * 10 + '\033[1;30;44mSISTEMA ENGINSTOCK:\033[m' + " " * 23 + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " * 62 + "|")
    print("  " + "|" + " " * 21 + '\033[1mÁrea de Produtos:\033[m' + " " * 24 + "|")
    print("  " + "|" + " " * 20 + " " * 42 + "|")
    print("  " + "|" + " " * 18 + "1.1. Cadastrar Produto." + " " * 21 + "|")
    print("  " + "|" + " " * 18 + "1.2. Listar Produtos Cadastrados." + " " * 11 + "|")
    print("  " + "|" + " " * 18 + "1.3. Buscar Produto Cadastrado." + " " * 13 + "|")
    print("  " + "|" + " " * 18 + "1.4. Alterar Dados de Produto." + " " * 14 + "|")
    print("  " + "|" + " " * 18 + "1.5. Deletar Produto." + " " * 23 + "|")
    print("  " + "|" + " " * 18 + "1.6. Voltar." + " " * 32 + "|")
    print("  " + "|" + " " * 18 + "1.7. Encerrar Sistema." + " " * 22 + "|")
    print("  " + "|" + " " * 62 + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print()
    print()


def menu_estoque():

    os.system('cls')
    print()
    print()
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + "  " * 10 + '\033[1;30;44mSISTEMA ENGINSTOCK:\033[m' + " " * 23 + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " * 62 + "|")
    print("  " + "|" + " " * 21 + '\033[1mÁrea de Estoque:\033[m' + " " * 25 + "|")
    print("  " + "|" + " " * 20 + " " * 42 + "|")
    print("  " + "|" + " " * 14 + "2.1. Cadastro Dias em Estoque." + " " * 18 + "|")
    print("  " + "|" + " " * 14 + "2.2. Listar Produtos no Estoque." + " " * 16 + "|")
    print("  " + "|" + " " * 14 + "2.3. Buscar Produto em Estoque." + " " * 17 + "|")
    print("  " + "|" + " " * 14 + "2.4. Alterar informações de estoque." + " " * 12 + "|")
    print("  " + "|" + " " * 14 + "2.5. Deletar Produtos com Provisão 100%." + " " * 8 + "|")
    print("  " + "|" + " " * 14 + "2.6. Voltar." + " " * 36 + "|")
    print("  " + "|" + " " * 14 + "2.7. Encerrar Sistema." + " " * 26 + "|")
    print("  " + "|" + " " * 62 + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print()
    print()


def menu_compras():

    print()
    print()
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + "  " * 10 + '\033[1;30;44mSISTEMA ENGINSTOCK:\033[m' + " " * 23 + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " * 62 + "|")
    print("  " + "|" + " " * 21 + '\033[1mÁrea de Compras:\033[m' + " " * 25 + "|")
    print("  " + "|" + " " * 20 + " " * 42 + "|")
    print("  " + "|" + " " * 17 + "3.1. Cadastrar Compra." + " " * 23 + "|")
    print("  " + "|" + " " * 17 + "3.2. Listar Histórico Compras." + " " * 15 + "|")
    print("  " + "|" + " " * 17 + "3.3. Buscar Compra Cadastrada." + " " * 15 + "|")
    print("  " + "|" + " " * 17 + "3.4. Atualizar Compra." + " " * 23 + "|")
    print("  " + "|" + " " * 17 + "3.5. Deletar Compra." + " " * 25 + "|")
    print("  " + "|" + " " * 17 + "3.6. Voltar." + " " * 33 + "|")
    print("  " + "|" + " " * 17 + "3.7. Encerrar Sistema." + " " * 23 + "|")
    print("  " + "|" + " " * 62 + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print()
    print()


def menu_fornecedores():

    os.system('cls')
    print()
    print()
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + "  " * 10 + '\033[1;30;44mSISTEMA ENGINSTOCK:\033[m' + " " * 23 + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " * 62 + "|")
    print("  " + "|" + " " * 20 + '\033[1mÁrea de Fornecedores:\033[m' + " " * 21 + "|")
    print("  " + "|" + " " * 20 + " " * 42 + "|")
    print("  " + "|" + " " * 17 + "4.1. Cadastrar Fornecedores." + " " * 17 + "|")
    print("  " + "|" + " " * 17 + "4.2. Listar Fornecedores." + " " * 20 + "|")
    print("  " + "|" + " " * 17 + "4.3. Buscar Fornecedor Cadastrado." + " " * 11 + "|")
    print("  " + "|" + " " * 17 + "4.4. Alterar Dados de Fornecedores." + " " * 10 + "|")
    print("  " + "|" + " " * 17 + "4.5. Deletar Fornecedor." + " " * 21 + "|")
    print("  " + "|" + " " * 17 + "4.6. Voltar." + " " * 33 + "|")
    print("  " + "|" + " " * 17 + "4.7. Encerrar Sistema." + " " * 23 + "|")
    print("  " + "|" + " " * 62 + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print()
    print()


def menu_clientes():

    os.system('cls')
    print()
    print()
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + "  " * 10 + '\033[1;30;44mSISTEMA ENGINSTOCK:\033[m' + " " * 23 + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " * 62 + "|")
    print("  " + "|" + " " * 20 + '\033[1mÁrea de Clientes:\033[m' + " " * 25 + "|")
    print("  " + "|" + " " * 20 + " " * 42 + "|")
    print("  " + "|" + " " * 17 + "5.1. Cadastrar Clientes." + " " * 21 + "|")
    print("  " + "|" + " " * 17 + "5.2. Listar Clientes." + " " * 24 + "|")
    print("  " + "|" + " " * 17 + "5.3. Buscar Cliente Cadastrado." + " " * 14 + "|")
    print("  " + "|" + " " * 17 + "5.4. Alterar Dados de Clientes." + " " * 14 + "|")
    print("  " + "|" + " " * 17 + "5.5. Deletar Cliente." + " " * 24 + "|")
    print("  " + "|" + " " * 17 + "5.6. Voltar." + " " * 33 + "|")
    print("  " + "|" + " " * 17 + "5.7. Encerrar Sistema." + " " * 23 + "|")
    print("  " + "|" + " " * 62 + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print()
    print()