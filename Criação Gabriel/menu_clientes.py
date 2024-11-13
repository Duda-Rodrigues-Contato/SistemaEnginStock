def main():
    while True:
        print("=== CRUD de Clientes ===")
        print("1. Criar Cliente")
        print("2. Atualizar Cliente")
        print("3. Deletar Cliente")
        print("4. Listar Clientes")
        print("5. Sair")
        
        escolha = input("Escolha uma opção (1-5): ").strip()
        
        if escolha == '1':
            create_client()
        elif escolha == '2':
            update_client()
        elif escolha == '3':
            delete_client()
        elif escolha == '4':
            list_clients()
        elif escolha == '5':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha entre 1 e 5.\n")

if __name__ == "__main__":
    main()