import json
import os
import re  # Biblioteca para expressões regulares

# Caminho do arquivo JSON para armazenar dados dos fornecedores
ARQUIVO_FORNECEDORES = 'fornecedores.json'

def nome_sistema():
    print('----- Sistema Fornecedores -----')

def menu():
    print('1- Cadastrar fornecedores')
    print('2- Listar fornecedores')
    print('3- Atualizar dados de um fornecedor já existente')
    print('4- Deletar fornecedores')
    print('5- Voltar')
    print('6- Sair')

def carregar_fornecedores():
    """Carrega os fornecedores do arquivo JSON"""
    if os.path.exists(ARQUIVO_FORNECEDORES):
        with open(ARQUIVO_FORNECEDORES, 'r') as file:
            return json.load(file)
    return {}

def salvar_fornecedores(fornecedores):
    """Salva os fornecedores no arquivo JSON"""
    with open(ARQUIVO_FORNECEDORES, 'w') as file:
        json.dump(fornecedores, file, indent=4)

def validar_cnpj(cnpj):
    """Valida o formato do CNPJ no padrão XX.XXX.XXX/XXXX-XX"""
    # Expressão regular para o formato do CNPJ
    padrao = r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'
    return bool(re.match(padrao, cnpj))

def cadastrar_fornecedor(fornecedores):
    """Cadastra um novo fornecedor no dicionário"""
    nome_do_fornecedor = input('Informe o nome do fornecedor: ')
    
    # Solicita o CNPJ e valida o formato
    while True:
        cnpj = input('Informe o CNPJ do fornecedor (formato XX.XXX.XXX/XXXX-XX): ')
        if validar_cnpj(cnpj):
            break
        else:
            print('CNPJ inválido. Por favor, digite no formato XX.XXX.XXX/XXXX-XX.')
    
    tempo_de_entrega = int(input('Informe o tempo de entrega dos produtos do fornecedor (em dias): '))
    
    # Verifica se o CNPJ já existe
    if cnpj in fornecedores:
        print('Este CNPJ já está cadastrado.')
        return
    
    fornecedores[cnpj] = {
        "nome": nome_do_fornecedor,
        "tempo_de_entrega": tempo_de_entrega
    }
    
    print('Cadastro realizado com sucesso!')
    salvar_fornecedores(fornecedores)

def listar_fornecedores(fornecedores):
    """Lista todos os fornecedores"""
    if not fornecedores:
        print('Nenhum fornecedor cadastrado.')
    else:
        print('----- Lista de Fornecedores -----')
        for cnpj, dados in fornecedores.items():
            print(f'CNPJ: {cnpj}')
            print(f'Nome: {dados["nome"]}')
            print(f'Tempo de Entrega: {dados["tempo_de_entrega"]} dias')
            print('-------------------------------')

def atualizar_fornecedor(fornecedores):
    """Atualiza os dados de um fornecedor existente"""
    cnpj = input('Informe o CNPJ do fornecedor que deseja atualizar: ')
    
    if cnpj not in fornecedores:
        print('Fornecedor não encontrado.')
        return
    
    nome_do_fornecedor = input('Informe o novo nome do fornecedor: ')
    tempo_de_entrega = int(input('Informe o novo tempo de entrega dos produtos do fornecedor (em dias): '))
    
    fornecedores[cnpj] = {
        "nome": nome_do_fornecedor,
        "tempo_de_entrega": tempo_de_entrega
    }
    
    print('Fornecedor atualizado com sucesso!')
    salvar_fornecedores(fornecedores)

def deletar_fornecedor(fornecedores):
    """Deleta um fornecedor do dicionário"""
    cnpj = input('Informe o CNPJ do fornecedor que deseja deletar: ')
    
    if cnpj in fornecedores:
        del fornecedores[cnpj]
        print('Fornecedor deletado com sucesso!')
        salvar_fornecedores(fornecedores)
    else:
        print('Fornecedor não encontrado.')

def escolha(fornecedores):
    """Realiza a escolha de uma ação no menu"""
    opcao = input('Escolha uma das opções acima: ')
    
    match opcao:
        case '1': 
            cadastrar_fornecedor(fornecedores)
        case '2':
            listar_fornecedores(fornecedores)
        case '3':
            atualizar_fornecedor(fornecedores)
        case '4':
            deletar_fornecedor(fornecedores)
        case '5':
            print('Voltando ao menu inicial...')
            return False  
        case '6':
            print('Saindo do sistema...')
            return False  
        case _:
            print('Opção inválida, por favor, escolha uma opção válida.')
    
    return True  

def main():
    fornecedores = carregar_fornecedores()
    while True:  
        nome_sistema()
        menu()
        if not escolha(fornecedores):  
            break

if __name__ == '__main__':
    main()