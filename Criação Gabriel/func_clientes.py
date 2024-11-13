import os
import json
import re

def create_client():
    caminho_arquivo = "D:/GitHub/studies-python/Cesar/trabalho aeda clientes/clientes.json"
    
    # Carrega os dados existentes no arquivo, se houver
    dados_existentes = []
    if os.path.exists(caminho_arquivo) and os.path.getsize(caminho_arquivo) > 0:
        with open(caminho_arquivo, "r") as arquivo:
            dados_existentes = json.load(arquivo)

    while True:
        # Verifica se o CNPJ é válido e não duplicado
        while True:
            cnpj = input("Digite o CNPJ do cliente (14 dígitos): ")
            cnpj = re.sub(r'[^0-9]', '', cnpj)  # Remove caracteres especiais
            if not (cnpj.isdigit() and len(cnpj) == 14):
                print("CNPJ inválido. Certifique-se de que contém 14 dígitos numéricos.")
                continue
            if any(cliente["cnpj"] == cnpj for cliente in dados_existentes):
                print("Já existe um cliente com esse CNPJ. Digite um CNPJ diferente.")
            else:
                break

        # Verifica se o telefone é válido e não duplicado
        while True:
            telefone = input("Digite o telefone do cliente (9 dígitos, começando com 9): ")
            if not (telefone.isdigit() and len(telefone) == 9 and telefone.startswith('9')):
                print("Telefone inválido. Certifique-se de que contém 9 dígitos e comece com 9.")
                continue
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

        # Remove caracteres especiais antes de buscar o cliente
        cnpj_cliente = re.sub(r'[^0-9]', '', cnpj_cliente)
        
        cliente_encontrado = False
        for cliente in dados_existentes:
            if cliente["cnpj"] == cnpj_cliente:
                cliente_encontrado = True
                print("\nCliente encontrado. Deixe em branco para manter o valor atual.")
                
                cliente["nome"] = input(f"Nome [{cliente['nome']}]: ") or cliente["nome"]
                
                while True:
                    novo_cnpj = input(f"CNPJ [{cliente['cnpj']}]: ") or cliente["cnpj"]
                    novo_cnpj = re.sub(r'[^0-9]', '', novo_cnpj)  # Remove caracteres especiais
                    if not (novo_cnpj.isdigit() and len(novo_cnpj) == 14):
                        print("CNPJ inválido. Certifique-se de que contém 14 dígitos numéricos.")
                        continue
                    cliente["cnpj"] = novo_cnpj
                    break

                while True:
                    novo_telefone = input(f"Telefone [{cliente['telefone']}]: ") or cliente["telefone"]
                    if not (novo_telefone.isdigit() and len(novo_telefone) == 9 and novo_telefone.startswith('9')):
                        print("Telefone inválido. Certifique-se de que contém 9 dígitos e comece com 9.")
                        continue
                    cliente["telefone"] = novo_telefone
                    break

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

    # Remove caracteres especiais do CNPJ antes de verificar
    cnpj_cliente = re.sub(r'[^0-9]', '', cnpj_cliente)

    if not (cnpj_cliente.isdigit() and len(cnpj_cliente) == 14):
        print("CNPJ inválido. Certifique-se de que contém 14 dígitos numéricos.")
        return

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
        # Formatar o CNPJ para exibição
        cnpj_formatado = f"{cliente['cnpj'][:2]}.{cliente['cnpj'][2:5]}.{cliente['cnpj'][5:8]}/{cliente['cnpj'][8:12]}-{cliente['cnpj'][12:]}"
        print(f"Nome: {cliente['nome']}")
        print(f"CNPJ: {cnpj_formatado}")
        print(f"Telefone: {cliente['telefone']}")
        print("-" * 30)

create_client()
update_client()
delete_client()
list_clients()