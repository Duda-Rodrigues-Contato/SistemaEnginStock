import json
import re

# Função para carregar dados de um arquivo JSON (simula um banco de dados)
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

# Função para salvar dados em um arquivo JSON
def salvar_dados(arquivo, dados):
    with open(arquivo, "w") as f:
        json.dump(dados, f, indent=4)

# Caminho do arquivo JSON
ESTOQUE_JSON = "estoque.json"

# Carrega os dados do estoque
estoque = carregar_dados(ESTOQUE_JSON)

# Função para validar o formato do código do produto
def validar_codigo_produto(codigo_produto):
    return bool(re.match(r'^P\d{3}$', codigo_produto))

# Função para cadastrar o número de dias no estoque e as informações de estoque
def cadastro_dias_estoque():
    while True:
        try:
            codigo_produto = input("Digite o código do produto (formato P001): ").strip()

            # Valida o formato do código do produto
            if not validar_codigo_produto(codigo_produto):
                print("Código do produto inválido! O formato correto é P001, P002, etc.")
                continue

            # Verifica se o código do produto já existe no estoque
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
            
            # Valida o número de dias parado (somente inteiro)
            while True:
                try:
                    dias_parado = int(input("Digite o número de dias parado no estoque: "))
                    if dias_parado < 0:
                        print("O número de dias não pode ser negativo. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Erro: O número de dias deve ser um valor inteiro.")

            # Valida os valores numéricos para estoque mínimo, máximo e consumo mensal (somente números inteiros ou flutuantes)
            while True:
                try:
                    estoque_minimo = float(input("Digite o estoque mínimo: "))
                    if estoque_minimo < 0:
                        print("O estoque mínimo não pode ser negativo. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Erro: O estoque mínimo deve ser um número válido.")

            while True:
                try:
                    consumo_mensal = float(input("Digite o consumo mensal: "))
                    if consumo_mensal < 0:
                        print("O consumo mensal não pode ser negativo. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Erro: O consumo mensal deve ser um número válido.")
            
            while True:
                try:
                    estoque_maximo = float(input("Digite o estoque máximo: "))
                    if estoque_maximo < 0:
                        print("O estoque máximo não pode ser negativo. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Erro: O estoque máximo deve ser um número válido.")

            # Valida o estoque de segurança (somente números inteiros ou flutuantes)
            while True:
                try:
                    estoque_seguranca = float(input("Digite o estoque de segurança: "))
                    if estoque_seguranca < 0:
                        print("O estoque de segurança não pode ser negativo. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Erro: O estoque de segurança deve ser um número válido.")

            # Salva os dados no estoque
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

# Função para listar produtos com mais de 180 dias parados no estoque (100% em provisão)
def listar_produtos_100_provisao():
    print("\nProdutos com mais de 180 dias parados no estoque (100% em provisão):")
    produtos_100_provisao = False  # Flag para verificar se encontrou algum produto
    for codigo, dados in estoque.items():
        dias_parado = dados['dias_parado']
        if dias_parado > 180:
            produto_nome = dados.get('nome', 'Produto desconhecido')
            print(f"Produto: {produto_nome} | Código: {codigo} | Dias Parado: {dias_parado} dias")
            produtos_100_provisao = True  # Indicando que encontrou pelo menos um produto
    if not produtos_100_provisao:
        print("Nenhum produto encontrado com mais de 180 dias parado no estoque.")

# Função para deletar produtos com mais de 180 dias parados no estoque
def deletar_produtos_100_provisao():
    listar_produtos_100_provisao()  # Exibe a lista de produtos
    produtos_para_deletar = [codigo for codigo, dados in estoque.items() if dados['dias_parado'] > 180]
    
    if produtos_para_deletar:
        print("\nDigite o código do produto que você deseja deletar ou 'cancelar' para voltar.")
        codigo_deletar = input("Código do produto a deletar: ").strip()
        
        if codigo_deletar in produtos_para_deletar:
            del estoque[codigo_deletar]
            salvar_dados(ESTOQUE_JSON, estoque)
            print(f"Produto {codigo_deletar} deletado com sucesso!")
        elif codigo_deletar.lower() == 'cancelar':
            print("Operação de deletação cancelada.")
        else:
            print("Código de produto inválido.")
    else:
        print("Nenhum produto encontrado para deletar.")

# Função para atualizar as informações do estoque (estoque mínimo, máximo, consumo mensal, estoque de segurança e dias parado)
def atualizar_informacoes_estoque(codigo_produto):
    print("\nAtualização de informações de estoque (estoque mínimo, máximo, consumo mensal, estoque de segurança e dias parado):")
    while True:
        try:
            # Atualiza o número de dias parado (somente inteiro)
            while True:
                try:
                    dias_parado = int(input(f"Digite o número de dias parado no estoque para o produto {codigo_produto}: "))
                    if dias_parado < 0:
                        print("O número de dias não pode ser negativo. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Erro: O número de dias deve ser um valor inteiro.")
            
            # Atualiza os valores numéricos para estoque mínimo, máximo e consumo mensal (somente números inteiros ou flutuantes)
            while True:
                try:
                    estoque_minimo = float(input("Digite o estoque mínimo: "))
                    if estoque_minimo < 0:
                        print("O estoque mínimo não pode ser negativo. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Erro: O estoque mínimo deve ser um número válido.")

            while True:
                try:
                    consumo_mensal = float(input("Digite o consumo mensal: "))
                    if consumo_mensal < 0:
                        print("O consumo mensal não pode ser negativo. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Erro: O consumo mensal deve ser um número válido.")
            
            while True:
                try:
                    estoque_maximo = float(input("Digite o estoque máximo: "))
                    if estoque_maximo < 0:
                        print("O estoque máximo não pode ser negativo. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Erro: O estoque máximo deve ser um número válido.")

            # Atualiza o estoque de segurança (somente números inteiros ou flutuantes)
            while True:
                try:
                    estoque_seguranca = float(input("Digite o estoque de segurança: "))
                    if estoque_seguranca < 0:
                        print("O estoque de segurança não pode ser negativo. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Erro: O estoque de segurança deve ser um número válido.")

            # Atualiza as informações no estoque
            estoque[codigo_produto].update({
                'dias_parado': dias_parado,
                'estoque_minimo': estoque_minimo,
                'consumo_mensal': consumo_mensal,
                'estoque_maximo': estoque_maximo,
                'estoque_seguranca': estoque_seguranca
            })
            salvar_dados(ESTOQUE_JSON, estoque)
            print(f"Informações do produto {codigo_produto} atualizadas com sucesso!")
            break
        except ValueError:
            print("Erro: Digite valores válidos.")


# Função para exibir o menu principal
def menu_principal():
    while True:
        print("\nMenu de Estoque:")
        print("1 - Cadastro de número de dias em estoque")
        print("2 - Atualizar informações de estoque")
        print("3 - Listar produtos com 100% em provisão (mais de 180 dias parado no estoque)")
        print("4 - Deletar produtos com 100% de provisão")
        print("5 - Voltar para o menu principal")
        print("6 - Encerrar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastro_dias_estoque()
        elif opcao == "2":
            codigo_produto = input("Digite o código do produto a ser atualizado: ").strip()
            if codigo_produto in estoque:
                atualizar_informacoes_estoque(codigo_produto)
            else:
                print("Produto não encontrado.")
        elif opcao == "3":
            listar_produtos_100_provisao()
        elif opcao == "4":
            deletar_produtos_100_provisao()
        elif opcao == "5":
            print("Voltando para o menu principal...")
            break
        elif opcao == "6":
            print("Encerrando o programa...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu_principal()
