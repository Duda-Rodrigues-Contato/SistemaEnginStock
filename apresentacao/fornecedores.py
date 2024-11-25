import json
import os
import re  # Biblioteca para expressões regulares


ARQUIVO_FORNECEDORES = 'fornecedores.json'

def nome_sistema():
    print('----- Sistema Fornecedores -----')

def menu():
    print('1- Cadastrar fornecedores')
    print('2- Listar fornecedores')
    print('3- Atualizar dados de um fornecedor já existente')
    print('4- Deletar fornecedores')
    print('5- Buscar fornecedor pelo CNPJ')
    print('6- Voltar')
    print('7- Sair')

def carregar_fornecedores():
  
    if os.path.exists(ARQUIVO_FORNECEDORES):
        with open(ARQUIVO_FORNECEDORES, 'r') as file:
            return json.load(file)
    return {}

def salvar_fornecedores(fornecedores):
    
    with open(ARQUIVO_FORNECEDORES, 'w') as file:
        json.dump(fornecedores, file, indent=4)

def validar_cnpj(cnpj):
    
    padrao = r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'
    return bool(re.match(padrao, cnpj))

def cadastrar_fornecedor(fornecedores):
    
    nome_do_fornecedor = input('Informe o nome do fornecedor: ')
    
    
    while True:
        cnpj = input('Informe o CNPJ do fornecedor (formato XX.XXX.XXX/XXXX-XX): ')
        if validar_cnpj(cnpj):
            break
        else:
            print('CNPJ inválido. Por favor, digite no formato XX.XXX.XXX/XXXX-XX.')
    
    tempo_de_entrega = int(input('Informe o tempo de entrega dos produtos do fornecedor (em dias): '))
    
    
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
    
    cnpj = input('Informe o CNPJ do fornecedor que deseja deletar: ')
    
    if cnpj in fornecedores:
        del fornecedores[cnpj]
        print('Fornecedor deletado com sucesso!')
        salvar_fornecedores(fornecedores)
    else:
        print('Fornecedor não encontrado.')

def buscar_fornecedor_por_cnpj(fornecedores):
    
    cnpj = input('Informe o CNPJ do fornecedor que deseja buscar: ')
    
    if cnpj in fornecedores:
        print('----- Dados do Fornecedor -----')
        print(f'CNPJ: {cnpj}')
        print(f'Nome: {fornecedores[cnpj]["nome"]}')
        print(f'Tempo de Entrega: {fornecedores[cnpj]["tempo_de_entrega"]} dias')
        print('--------------------------------')
    else:
        print('Fornecedor não encontrado.')

def escolha(fornecedores):
    
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
            buscar_fornecedor_por_cnpj(fornecedores)
        case '6':
            print('Voltando ao menu inicial...')
            return False  
        case '7':
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
