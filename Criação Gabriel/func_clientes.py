import os
import json

def create_client():
    caminho_arquivo = "D:/GitHub/studies-python/Cesar/trabalho aeda clientes/clientes.json"
    
    # Carrega os dados existentes no arquivo, se houver
    dados_existentes = []
    if os.path.exists(caminho_arquivo) and os.path.getsize(caminho_arquivo) > 0:
        with open(caminho_arquivo, "r") as arquivo:
            dados_existentes = json.load(arquivo)

    while True:
                
        # Verifica se o CNPJ já existe
        while True:
            cnpj = input("Digite o CNPJ do cliente: ")
            if any(cliente["cnpj"] == cnpj for cliente in dados_existentes):
                print("Já existe um cliente com esse CNPJ. Digite um CNPJ diferente.")
            else:
                break

        # Verifica se o telefone já existe
        while True:
            telefone = input("Digite o telefone do cliente: ")
            if any(cliente["telefone"] == telefone for cliente in dados_existentes):
                print("Já existe um cliente com esse telefone. Digite um telefone diferente.")
            else:
                break

        cliente = {
            "nome": input("Digite o nome do cliente: "),
            "cnpj": cnpj,
            "telefone": telefone
        }

        dados_existentes.append(cliente)

        # Salva os dados
        with open(caminho_arquivo, "w") as arquivo:
            json.dump(dados_existentes, arquivo, indent=4)

        print("\nCliente salvo com sucesso:")
        print(f"Nome: {cliente['nome']}")
        print(f"CNPJ: {cliente['cnpj']}")
        print(f"Telefone: {cliente['telefone']}")

        # Pergunta se o usuário deseja cadastrar outro cliente
        continuar = input("\nDeseja cadastrar outro cliente? (s/n): ").strip().lower()
        if continuar != 's':
            print("Cadastro encerrado.")
            break

def update_client():
    caminho_arquivo = "D:/GitHub/studies-python/Cesar/trabalho aeda clientes/clientes.json"
    
    if os.path.exists(caminho_arquivo) and os.path.getsize(caminho_arquivo) > 0:
        with open(caminho_arquivo, "r") as arquivo:
            dados_existentes = json.load(arquivo)
    else:
        print("Nenhum cliente encontrado.")
        return

    while True:
        cnpj_cliente = input("Digite o CNPJ do cliente que deseja atualizar (ou 'sair' para cancelar): ")
        if cnpj_cliente.lower() == 'sair':
            print("Operação cancelada.")
            return

        cliente_encontrado = False
        for cliente in dados_existentes:
            if cliente["cnpj"] == cnpj_cliente:
                cliente_encontrado = True
                print("\nCliente encontrado. Deixe em branco para manter o valor atual.")
                
                cliente["nome"] = input(f"Nome [{cliente['nome']}]: ") or cliente["nome"]
                
                novo_cnpj = input(f"CNPJ [{cliente['cnpj']}]: ") or cliente["cnpj"]
                cliente["cnpj"] = novo_cnpj
                
                cliente["telefone"] = input(f"Telefone [{cliente['telefone']}]: ") or cliente["telefone"]

                # Salvar dados atualizados no arquivo JSON
                with open(caminho_arquivo, "w") as arquivo:
                    json.dump(dados_existentes, arquivo, indent=4)

                print("\nCliente atualizado com sucesso!")
                print(f"Nome: {cliente['nome']}")
                print(f"CNPJ: {cliente['cnpj']}")
                print(f"Telefone: {cliente['telefone']}")

                return cliente
        
        if not cliente_encontrado:
            print("Cliente com CNPJ especificado não encontrado. Tente novamente.")

def delete_client():
    caminho_arquivo = "D:/GitHub/studies-python/Cesar/trabalho aeda clientes/clientes.json"
    
    # Carregar dados existentes
    if os.path.exists(caminho_arquivo) and os.path.getsize(caminho_arquivo) > 0:
        with open(caminho_arquivo, "r") as arquivo:
            dados_existentes = json.load(arquivo)
    else:
        print("Nenhum cliente encontrado.")
        return

    cnpj_cliente = input("Digite o CNPJ do cliente que deseja excluir: ")

    # Procurar e excluir
    cliente_encontrado = False
    for i, cliente in enumerate(dados_existentes):
        if cliente["cnpj"] == cnpj_cliente:
            cliente_encontrado = True
            del dados_existentes[i]
            print(f"\nCliente com CNPJ {cnpj_cliente} excluído com sucesso.")
            break

    if not cliente_encontrado:
        print("Cliente com o CNPJ especificado não encontrado.")
        return

    # Salvar os dados atualizados
    with open(caminho_arquivo, "w") as arquivo:
        json.dump(dados_existentes, arquivo, indent=4)


def list_clients():
    caminho_arquivo = "D:/GitHub/studies-python/Cesar/trabalho aeda clientes/clientes.json"
    
    # Verifica se o arquivo existe e contém dados
    if os.path.exists(caminho_arquivo) and os.path.getsize(caminho_arquivo) > 0:
        with open(caminho_arquivo, "r") as arquivo:
            dados_existentes = json.load(arquivo)
    else:
        print("Nenhum cliente encontrado.")
        return

    # Exibe a lista com todos os clientes
    print("\nLista de Clientes:")
    for cliente in dados_existentes:
        print(f"Nome: {cliente['nome']}")
        print(f"CNPJ: {cliente['cnpj']}")
        print(f"Telefone: {cliente['telefone']}")
        print("-" * 30)

delete_client()
list_clients()