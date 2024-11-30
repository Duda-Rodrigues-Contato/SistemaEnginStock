import json
import re

def carregar_dados(arquivo):
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Arquivo não encontrado. Criando um novo arquivo vazio.")
        return {}
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON. Criando um novo arquivo vazio.")
        return {}

def salvar_dados(arquivo, dados):
    with open(arquivo, "w") as f:
        json.dump(dados, f, indent=4)

ESTOQUE_JSON = "estoque.json"

estoque = carregar_dados(ESTOQUE_JSON)

def validar_codigo_produto(codigo_produto):
    return bool(re.match(r'^P\d{3}$', codigo_produto))

def listar_todos_produtos():
    print("\nLista de Todos os Produtos no Estoque:")
    if not estoque:
        print("Nenhum produto encontrado no estoque.")
    else:
        for codigo, dados in estoque.items():
            print(f"Produto: {dados['nome']} | Código: {codigo} | Dias Parado: {dados['dias_parado']} dias")
            print(f"Estoque Mínimo: {dados['estoque_minimo']} | Estoque Máximo: {dados['estoque_maximo']}")
            print(f"Consumo Mensal: {dados['consumo_mensal']} | Estoque de Segurança: {dados['estoque_seguranca']}")
            print("-" * 50)

def buscar_produtos_180_dias():
    print("\nProdutos com exatamente 180 dias parados no estoque:")
    encontrados = False
    for codigo, dados in estoque.items():
        if dados['dias_parado'] == 180:
            print(f"Produto: {dados['nome']} | Código: {codigo} | Dias Parado: {dados['dias_parado']} dias")
            encontrados = True
    if not encontrados:
        print("Nenhum produto encontrado com exatamente 180 dias parados no estoque.")

def deletar_produtos_180_dias():
    print("\nProdutos com exatamente 180 dias parados no estoque:")
    produtos_para_deletar = [codigo for codigo, dados in estoque.items() if dados['dias_parado'] == 180]
    
    if produtos_para_deletar:
        for codigo in produtos_para_deletar:
            print(f"Produto: {estoque[codigo]['nome']} | Código: {codigo} | Dias Parado: {estoque[codigo]['dias_parado']} dias")
        confirmacao = input("Deseja deletar todos os produtos listados? (S/N): ").strip().lower()
        if confirmacao == 's':
            for codigo in produtos_para_deletar:
                del estoque[codigo]
            salvar_dados(ESTOQUE_JSON, estoque)
            print("Produtos com exatamente 180 dias no estoque deletados com sucesso!")
        else:
            print("Operação de deletar produtos cancelada.")
    else:
        print("Nenhum produto encontrado com exatamente 180 dias parados no estoque.")

def cadastro_dias_estoque():
    while True:
        try:
            codigo_produto = input("Digite o código do produto (formato P001): ").strip()
           
            if not validar_codigo_produto(codigo_produto):
                print("Código do produto inválido! O formato correto é P001, P002, etc.")
                continue
           
            if codigo_produto in estoque:
                print(f"Produto com o código {codigo_produto} já cadastrado!")
                atualizar = input("Deseja atualizar as informações deste produto? (S/N): ").strip().lower()
                if atualizar == 's':
                    atualizar_informacoes_estoque(codigo_produto)
                    return
                else:
                    print("Cadastro de novo produto cancelado.")
                    return
            nome_produto = input("Digite o nome do produto: ").strip()
            dias_parado = int(input("Digite o número de dias parado no estoque: "))
            estoque_minimo = float(input("Digite o estoque mínimo: "))
            consumo_mensal = float(input("Digite o consumo mensal: "))
            estoque_maximo = float(input("Digite o estoque máximo: "))
            estoque_seguranca = float(input("Digite o estoque de segurança: "))
           
            estoque[codigo_produto] = {
                'nome': nome_produto,
                'dias_parado': dias_parado,
                'estoque_minimo': estoque_minimo,
                'consumo_mensal': consumo_mensal,
                'estoque_maximo': estoque_maximo,
                'estoque_seguranca': estoque_seguranca
            }
            salvar_dados(ESTOQUE_JSON, estoque)
            print(f"Produto {nome_produto} cadastrado com sucesso!")
            break
        except ValueError:
            print("Erro: Digite valores válidos.")

def atualizar_informacoes_estoque(codigo_produto):
    if codigo_produto in estoque:
        print(f"Atualizando informações para o produto {codigo_produto} - {estoque[codigo_produto]['nome']}")
        estoque[codigo_produto]['dias_parado'] = int(input("Digite o novo número de dias parado: "))
        estoque[codigo_produto]['estoque_minimo'] = float(input("Digite o novo estoque mínimo: "))
        estoque[codigo_produto]['consumo_mensal'] = float(input("Digite o novo consumo mensal: "))
        estoque[codigo_produto]['estoque_maximo'] = float(input("Digite o novo estoque máximo: "))
        estoque[codigo_produto]['estoque_seguranca'] = float(input("Digite o novo estoque de segurança: "))
        salvar_dados(ESTOQUE_JSON, estoque)
        print("Informações atualizadas com sucesso!")
    else:
        print("Produto não encontrado no estoque.")

def menu_principal():
    while True:
        print("\nMenu de Estoque:")
        print("1 - Cadastrar dias parado no Estoque")
        print("2 - Atualizar informações de um produto")
        print("3 - Listar todos os produtos em estoque")
        print("4 - Buscar produtos com exatamente 180 dias parados")
        print("5 - Deletar produtos com exatamente 180 dias parados")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastro_dias_estoque()
        elif opcao == "2":
            codigo_produto = input("Digite o código do produto a ser atualizado: ").strip()
            atualizar_informacoes_estoque(codigo_produto)
        elif opcao == "3":
            listar_todos_produtos()
        elif opcao == "4":
            buscar_produtos_180_dias()
        elif opcao == "5":
            deletar_produtos_180_dias()
        elif opcao == "6":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()
