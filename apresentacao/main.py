from produtos import *
from estoque import *
from clientes import *
from compras import*
from fornecedores import *
from menus import *
from uteis import *
from time import sleep
import os

def funcionamento_main():

    menu_boas_vindas()

    sleep(1.5)

    os.system('cls')

    menu_inicial()

    escolha_menu_principal = int(input('\033[1mDIGITE SUA ESCOLHA: \033[m'))

    match escolha_menu_principal:
        case 1:
            while True:
                menu_produtos()
                opcao_produtos = int(input('\033[1mDIGITE SUA ESCOLHA (APENAS O ÚLTIMO NÚMERO): \033[m'))

                match opcao_produtos:
                    case 1:
                        cadastro_produtos()
                    case 2:
                        listar_produtos()
                    case 3:
                        buscar_produto()
                    case 4:
                        atualizar_produtos()
                    case 5:
                        deletar_produtos()
                    case 6:
                        funcionamento_main()
                    case 7:
                        encerrar_sistema()
                    case _:
                        print("Opção Inválida!")
                        return
        case 2:
            while True:

                menu_estoque()
                opcao_estoque = float(input('\033[1mDIGITE SUA ESCOLHA (APENAS O ÚLTIMO NÚMERO): \033[m'))

                match opcao_estoque:
                    case 1:
                        cadastro_dias_estoque()
                    case 2:
                        listar_todos_produtos()
                    case 3:
                        buscar_produtos_180_dias()
                    case 4:
                        atualizar_informacoes_estoque()
                    case 5:
                        deletar_produtos_180_dias()
                    case 6:
                        funcionamento_main()
                    case 7:
                        encerrar_sistema()
                    case _:
                        print("Opção Inválida!")
                        return

        case 3:
            while True:
                menu_compras()   
                opcao_compras = int(input('\033[1mDIGITE SUA ESCOLHA (APENAS O ÚLTIMO NÚMERO): \033[m'))

                match opcao_compras:
                    case 1:
                        adicionar_compra()
                    case 2:
                        listar_compras()
                    case 3:
                        buscar_compra()
                    case 4:
                        alterar_compra()
                    case 5:
                        deletar_compra()
                    case 6:
                        funcionamento_main()
                    case 7:
                        encerrar_sistema()
                    case _:
                        print("Opção Inválida!")
                        return

        case 4:
            while True:

                menu_fornecedores()   
                opcao_fornecedores = int(input('\033[1mDIGITE SUA ESCOLHA (APENAS O ÚLTIMO NÚMERO): \033[m'))

                match opcao_fornecedores:
                    case 1:
                        cadastrar_fornecedor()
                    case 2:
                        listar_fornecedores()
                    case 3:
                        buscar_fornecedor_por_cnpj()
                    case 4:
                        atualizar_fornecedor()
                    case 5:
                        deletar_fornecedor()
                    case 6:
                        funcionamento_main()
                    case 7:
                        encerrar_sistema()
                    case _:
                        print("Opção Inválida!")
                        return

        case 5:
            while True:
                menu_clientes()

                opcao_clientes = int(input('\033[1mDIGITE SUA ESCOLHA (APENAS O ÚLTIMO NÚMERO): \033[m'))    

                match opcao_clientes:
                    case 1:
                        create_client()
                    case 2:
                        list_clients()
                    case 3:
                        buscar_cliente()
                    case 4:
                        update_client()
                    case 5:
                        delete_client()
                    case 6:
                        funcionamento_main()
                    case 7:
                        encerrar_sistema()
                    case _:
                        print("Opção Inválida!")
                        return
        
        case 6:   
            encerrar_sistema()

        case _:
            print("Opção Inválida!")
            print('\033[1;30;44mOBRIGADO POR ESCOLHER A ENGINSTOCK!\033[m')
            print('\033[1;30mENCERRANDO SISTEMA...\033[m')
            sleep(1.5)
            sys.exit()


funcionamento_main()