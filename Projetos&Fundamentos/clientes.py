import json
import os
import re



def carregar_dados(arquivo):
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Arquivo não encontrado. Criando um novo arquivo vazio.")
        return []
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON. Criando um novo arquivo vazio.")
        return []

def salvar_dados(arquivo, dados):
    with open(arquivo, "w") as f:
        json.dump(dados, f, indent=4)


def obter_caminho_arquivo():
    caminho_diretorio = os.path.expanduser("~")
    caminho_arquivo = os.path.join(caminho_diretorio, "clientes.json")
    return caminho_arquivo


def cadastrar_cliente():
    caminho_arquivo = obter_caminho_arquivo()
    dados_existentes = carregar_dados(caminho_arquivo)

    while True:
        while True:
            cnpj = input("Digite o CNPJ do cliente (14 dígitos): ")
            cnpj = re.sub(r'[^0-9]', '', cnpj)
            if not (cnpj.isdigit() and len(cnpj) == 14):
                print("CNPJ inválido. Certifique-se de que contém 14 dígitos numéricos.")
                continue
            else:
                break

        while True:
            telefone = input("Digite o telefone do cliente (9 dígitos, começando com 9): ")
            if not (telefone.isdigit() and len(telefone) == 9 and telefone.startswith('9')):
                print("Telefone inválido. Certifique-se de que contém 9 dígitos e começa com 9.")
                continue
            else:
                break

        nome = input("Digite o nome do cliente: ")

        cliente = {"nome": nome, "cnpj": cnpj, "telefone": telefone}

        dados_existentes.append(cliente)

        salvar_dados(caminho_arquivo, dados_existentes)

        print("\nCliente cadastrado com sucesso!")
        print(f"Nome: {cliente['nome']}")
        print(f"CNPJ: {cliente['cnpj']}")
        print(f"Telefone: {cliente['telefone']}")

        continuar = input("\nDeseja cadastrar outro cliente? (s/n): ").strip().lower()
        if continuar != 's':
            print("Cadastro encerrado.")
            break

def listar_clientes():
    caminho_arquivo = obter_caminho_arquivo()
    dados_existentes = carregar_dados(caminho_arquivo)

    if not dados_existentes:
        print("Nenhum cliente encontrado.")
        return

    print("\nLista de Clientes:")
    for cliente in dados_existentes:
        cnpj_formatado = f"{cliente['cnpj'][:2]}.{cliente['cnpj'][2:5]}.{cliente['cnpj'][5:8]}/{cliente['cnpj'][8:12]}-{cliente['cnpj'][12:]}"
        print(f"Nome: {cliente['nome']}")
        print(f"CNPJ: {cnpj_formatado}")
        print(f"Telefone: {cliente['telefone']}")
        print("-" * 30)

def buscar_cliente():
    caminho_arquivo = obter_caminho_arquivo()
    dados_existentes = carregar_dados(caminho_arquivo)

    if not dados_existentes:
        print("Nenhum cliente encontrado.")
        return

    busca = input("Digite o nome ou o CNPJ do cliente que deseja buscar: ").strip()
    busca = re.sub(r'[^0-9]', '', busca) if busca.isdigit() else busca.lower()

    cliente_encontrado = False
    for cliente in dados_existentes:
        if cliente["cnpj"] == busca or cliente["nome"].lower() == busca:
            cliente_encontrado = True
            cnpj_formatado = f"{cliente['cnpj'][:2]}.{cliente['cnpj'][2:5]}.{cliente['cnpj'][5:8]}/{cliente['cnpj'][8:12]}-{cliente['cnpj'][12:]}"
            print("\nCliente encontrado:")
            print(f"Nome: {cliente['nome']}")
            print(f"CNPJ: {cnpj_formatado}")
            print(f"Telefone: {cliente['telefone']}")
            print("-" * 30)
            break
    if not cliente_encontrado:
        print("\nCliente não encontrado. Verifique o nome ou CNPJ e tente novamente.")

def buscar_cliente_por_cnpj():
    caminho_arquivo = obter_caminho_arquivo()
    dados_existentes = carregar_dados(caminho_arquivo)

    if not dados_existentes:
        print("Nenhum cliente encontrado.")
        return

    cnpj = input("Digite o CNPJ do cliente que deseja buscar: ").strip()
    cnpj = re.sub(r'[^0-9]', '', cnpj)

    cliente_encontrado = False
    for cliente in dados_existentes:
        if cliente["cnpj"] == cnpj:
            cliente_encontrado = True
            print("\nCliente encontrado:")
            print(f"Nome: {cliente['nome']}")
            print(f"CNPJ: {cliente['cnpj']}")
            print(f"Telefone: {cliente['telefone']}")
            print("-" * 30)
            break
    if not cliente_encontrado:
        print("\nCliente com o CNPJ especificado não encontrado.")

def alterar_cliente():
    caminho_arquivo = obter_caminho_arquivo()
    dados_existentes = carregar_dados(caminho_arquivo)

    if not dados_existentes:
        print("Nenhum cliente encontrado.")
        return

    cnpj_cliente = input("Digite o CNPJ do cliente que deseja atualizar: ")
    cnpj_cliente = re.sub(r'[^0-9]', '', cnpj_cliente)

    cliente_encontrado = False
    for cliente in dados_existentes:
        if cliente["cnpj"] == cnpj_cliente:
            cliente_encontrado = True
            print("\nCliente encontrado. Atualize os campos abaixo ou pressione Enter para manter o valor atual.")

            while True:
                novo_cnpj = input(f"CNPJ [{cliente['cnpj']}]: ") or cliente["cnpj"]
                novo_cnpj = re.sub(r'[^0-9]', '', novo_cnpj)
                if not (novo_cnpj.isdigit() and len(novo_cnpj) == 14):
                    print("CNPJ inválido. Certifique-se de que contém 14 dígitos numéricos.")
                    continue
                cliente["cnpj"] = novo_cnpj
                break

            cliente["nome"] = input(f"Nome [{cliente['nome']}]: ") or cliente["nome"]

            while True:
                novo_telefone = input(f"Telefone [{cliente['telefone']}]: ") or cliente["telefone"]
                if not (novo_telefone.isdigit() and len(novo_telefone) == 9 and novo_telefone.startswith('9')):
                    print("Telefone inválido. Certifique-se de que contém 9 dígitos e começa com 9.")
                    continue
                cliente["telefone"] = novo_telefone
                break

            salvar_dados(caminho_arquivo, dados_existentes)

            print("\nCliente atualizado com sucesso!")
            break

    if not cliente_encontrado:
        print("\nCliente não encontrado.")

def deletar_cliente():
    caminho_arquivo = obter_caminho_arquivo()
    dados_existentes = carregar_dados(caminho_arquivo)

    if not dados_existentes:
        print("Nenhum cliente encontrado.")
        return

    cnpj_cliente = input("Digite o CNPJ do cliente que deseja excluir: ")
    cnpj_cliente = re.sub(r'[^0-9]', '', cnpj_cliente)

    cliente_encontrado = False
    for i, cliente in enumerate(dados_existentes):
        if cliente["cnpj"] == cnpj_cliente:
            cliente_encontrado = True
            print("\nCliente encontrado. Excluindo...")
            del dados_existentes[i]
            break

    if not cliente_encontrado:
        print("\nCliente não encontrado.")
        return

    salvar_dados(caminho_arquivo, dados_existentes)
    print("Cliente excluído com sucesso!")


def menu_clientes():
    print("\n" + "-" * 60)
    print(" " * 15 + "Sistema de Gestão de Clientes")
    print("-" * 60)
    print("  " + "|" + " " * 17 + "5.1. Cadastrar Clientes." + " " * 21 + "|")
    print("  " + "|" + " " * 17 + "5.2. Listar Clientes." + " " * 24 + "|")
    print("  " + "|" + " " * 17 + "5.3. Buscar Cliente Cadastrado." + " " * 14 + "|")
    print("  " + "|" + " " * 17 + "5.4. Alterar Dados de Clientes." + " " * 14 + "|")
    print("  " + "|" + " " * 17 + "5.5. Deletar Cliente." + " " * 24 + "|")
    print("  " + "|" + " " * 17 + "5.6. Buscar Cliente pelo CNPJ." + " " * 16 + "|")
    print("  " + "|" + " " * 17 + "5.7. Encerrar Sistema." + " " * 23 + "|")
    print("-" * 60)

def main():
    while True:
        menu_clientes()
        opcao = input("Escolha uma opção (5.1 a 5.7): ").strip()

        if opcao == "5.1":
            cadastrar_cliente()
        elif opcao == "5.2":
            listar_clientes()
        elif opcao == "5.3":
            buscar_cliente()
        elif opcao == "5.4":
            alterar_cliente()
        elif opcao == "5.5":
            deletar_cliente()
        elif opcao == "5.6":
            buscar_cliente_por_cnpj()
        elif opcao == "5.7":
            print("Encerrando sistema. Até mais!")
            exit()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
