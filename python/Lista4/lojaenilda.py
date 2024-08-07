estoque = [
    {'codigo': '1', 'descricao': 'Celular', 'quantidade': 10},
    {'codigo': '2', 'descricao': 'Fone de Ouvido', 'quantidade': 20},
    {'codigo': '3', 'descricao': 'Carregador', 'quantidade': 15}
]



while True:
    print('''Seja bem vindo 
    1. Adicionar produto 
    2. Vender produto 
    3. Verificar estoque 
    4. Sair ''')

    opcao = input("\nEscolha uma das opções acima: ")

    if opcao == '1':
        codigo = input("Digite o código do produto: ")
        descricao = input("Digite a descrição do produto: ")
        quantidade = int(input("Digite a quantidade do produto: "))
        
        produto_existente = next((p for p in estoque if p['codigo'] == codigo), None)
        if produto_existente:
            produto_existente['quantidade'] += quantidade
        else:
            novo_produto = {'codigo': codigo, 'descricao': descricao, 'quantidade': quantidade}
            estoque.append(novo_produto)
        
        print("Produto adicionado ao estoque.")

    elif opcao == '2':
        codigo = input("Digite o código do produto a ser vendido: ")
        quantidade = int(input("Digite a quantidade a ser vendida: "))
        for produto in estoque:
            if produto['codigo'] == codigo:
                if produto['quantidade'] >= quantidade:
                    produto['quantidade'] -= quantidade
                    print("Venda realizada com sucesso.")
                else:
                    print("Quantidade insuficiente em estoque.")
                break
        else:
            print("Produto não encontrado.")

    elif opcao == '3':
        print("\nEstoque disponível:")
        for produto in estoque:
            print(f"Código: {produto['codigo']}, Descrição: {produto['descricao']}, Quantidade: {produto['quantidade']}")
        
        print("\nEstoque adicionado:")
        for produto in estoque:
            print(f"Código: {produto['codigo']}, Descrição: {produto['descricao']}, Quantidade: {produto['quantidade']}")

    elif opcao == '4':
        print("Saindo.")
        break

    else:
        print("Opção inválida. Tente novamente.")
