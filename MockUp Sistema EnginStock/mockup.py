import os

class cor:
    NEGRITO = '\033[1m'
    AZUL = '\033[44m'
    RESET = "\033[0m"

def menu_principal():

    os.system('cls')
    print("=" * 60)
    print('-' * 60)
    print(cor.NEGRITO + cor.AZUL + "SISTEMA ENGINSTOCK:" + cor.RESET)
    print('-' * 60)
    print("=" * 60)
    print('-' * 60)
    print(cor.NEGRITO + "Menu Inicial:" + cor.RESET)
    print()
    print("1. Área de Produtos.")
    print("2. Área de Estoque.")
    print("3. Área de Compras")
    print("4. Área de Fornecedores.")
    print("5. Área de Clientes.")
    print("6. Encerrar Sistema.")
    print('-' * 60)
    print("=" * 60)
    print()


menu_principal()


def menu_compras():

    os.system('cls')
    print("=" * 60)
    print('-' * 60)
    print(cor.NEGRITO + cor.AZUL + "SISTEMA ENGINSTOCK:" + cor.RESET)
    print('-' * 60)
    print("=" * 60)
    print('-' * 60)
    print(cor.NEGRITO + "Área de Compras:" + cor.RESET)
    print()
    print("4.1 - Cadastrar Compra.")
    print("4.2 - Listar Compras.")
    print("4.3 - Atualizar Compra.")
    print("4.4 - Deletar Compra.")
    print("4.5 - Voltar.")
    print("4.6 - Encerrar Sistema.")
    print('-' * 60)
    print("=" * 60)
    print()

menu_compras()