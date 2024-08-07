produto_alimentos_frios = ['Margarina', 'polpa', 'carne']
codigo_alimentos_frios = ['000', '001', '002']
descricao_alimentos_frios = 'Categoria: Alimento, Subcategoria: Frios'
preco_a_f = ['9', '4', '37']
 
produto_alimentos_mercearia = ['Arroz ', 'Oléo ', 'Sal ']
codigo_alimentos_mercearia = ['00', '01', '02']
descricao_alimentos_mercearia = 'Categoria: Alimento, Subcategoria: Mercearia'
preco_a_m = ['25', '10', '4']
 
produto_limpeza = ['Sabaõ em pó', 'Detergente', 'Água sanitaria', 'Amaciante', ]
codigo_limpeza = ['0', '1', '2', '3', ]
descricao_limpeza = 'Categoria: Higiene, Subcategoria: Limpeza'
preco_p_l = ['17', '4', '8', '12',]
 
produto_higiene = ['creme dental', 'Condicionador', 'Desodorante', ]
codigo_higiene = [ '00', '01', '02']
descricao_higiene = 'Categoria: Higiene, Subcategoria: Pessoal'
preco_p_h = ['7','11', '18']
 
carrinho = []
carrinho_preco = []
total = 0
 
nome = input('Informe seu nome: ' )
cpf = input('Informe seu cpf:')
 
funcionario = input('Voce é funcionario do mercado? sim ou não: ')
if funcionario == 'sim':
    matricula = int(input('informe sua matricula: '))
    data_nascimento = input('informe sua data de nascimento (DD/MM/AAAA): ')
    print('Acesso autorizado como funcionario.')
    while True:
        entrada_usuario = ''
        print('digite a opção desejada: \n(1) para exibir estoque \n(2) para adicionar produto  \n(3) atualizar \n(4) para sair')
        entrada_usuario = input('Digite a opção desejada: ')
        if entrada_usuario == '1':
       
            for i in range(len(produto_alimentos_frios)):
                print('Nome:  ' + produto_alimentos_frios[i], ',Codigo: ' + codigo_alimentos_frios[i], ',Preço: R$ ' + str(preco_a_f[i]), ',Descrição: ' + descricao_alimentos_frios)
            print('\n')
            for i in range(len(produto_alimentos_mercearia)):
                print('Nome:  ' + produto_alimentos_mercearia[i], ',Codigo: ' + codigo_alimentos_mercearia[i], ',Preço: R$ ' + str(preco_a_m[i]), ',Descrição: ' + descricao_alimentos_mercearia)
            print('\n')
            for i in range(len(produto_limpeza)):
                print('Nome:  ' + produto_limpeza[i], ',Codigo: ' + codigo_limpeza[i], ',Preço: R$ ' + str(preco_p_l[i]), ',Descrição: ' + descricao_limpeza)
            print('\n')
            for i in range(len(produto_higiene)):
                print('Nome:  ' + produto_higiene[i], ',Codigo: ' + codigo_higiene[i], ',Preço: R$ ' + str(preco_p_h[i]), ',Descrição: ' + descricao_higiene)
 
        elif entrada_usuario == '2':
            print('Digite a opção desejada:'
                  '\n(1)para a categoria  alimentos frios',
                  '\n(2)digite para a categoria alimentos mercearia',
                  '\n(3)digite para a categoria produtos de higiene',
                  '\n(4)digite para a categoria produtos de limpeza')
            entrada2 = input('Digite o valor da categoria que deseja entrar ')
            if entrada2 == '1':
                produto_alimentos_frios.append(input('Digite o nome do novo produto '))
                codigo_alimentos_frios.append(input('Digite o código do novo produto '))
                preco_a_f.append(float(input('Digite o preço do produto ')))
            elif entrada2 == '2':
                produto_alimentos_mercearia.append(input('Digite o nome do novo produto '))
                codigo_alimentos_mercearia.append(input('Digite o codigo do novo produto '))
                preco_a_m.append(float(input('Digite o preço do novo produto ')))
            elif entrada2 == '3':
                produto_limpeza.append(input('Digite o nome do novo produto '))
                codigo_limpeza.append(input('Digite o codigo do novo produto '))
                preco_p_l.append(float(input('Digite o preço do novo produto ')))
            elif entrada2 == '4':
                produto_higiene.append(input('Digite o nome do novo produto '))
                codigo_higiene.append(input('Digite o codigo do novo produto '))
                preco_p_h.append(float(input('Digite o preço do novo produto ')))
            else:
                print('Digite a opção correta ')
        elif entrada_usuario == '3':
            pass
        elif entrada_usuario == '4':
            exit()
        else:
            print('Digite um opção válida!')
 
   
               
 
 
 
 
               
           
 
 
 
else:
    print('seja bem vindo cliente ')
 
    print("Produtos disponíveis:")
    print('alimentos frios')
    print(produto_alimentos_frios)
 
    while True:
        escolha = input("Digite o código do produto que deseja adicionar ao carrinho. \n'0800' - para proxima sessão. \n'70' - exit \n:")
        if escolha == '0800':
            break
        if escolha == '70':
            break
        else:
       
            carrinho.append(produto_alimentos_frios[int(escolha)])
            carrinho_preco.append(preco_a_f[int(escolha)])
            print(f"{produto_alimentos_frios[int(escolha)]} adicionado ao carrinho.")
            print(f'{preco_a_f[int(escolha)]}')
            print(f'valor total de todos os produtos R${preco_a_f[int(escolha)]}')
 
 
    print("Produtos disponíveis:")
    print('alimentos mercearia ')
    print(produto_alimentos_mercearia)
    while True:
        escolha = input("Digite o código do produto que deseja adicionar ao carrinho. \n'0800' - para proxima sessão. \n'70' - exit \n----->")
        if escolha == '0800':
            break
        if escolha == '70':
            break
        else:
            carrinho.append(produto_alimentos_mercearia[int(escolha)])
            carrinho_preco.append(preco_a_f[int(escolha)])
            print(f"{produto_alimentos_mercearia[int(escolha)]} adicionado ao carrinho.")
            print(f'{preco_a_m[int(escolha)]}')
            print(f'valor total de todos os produtos R${preco_a_m[int(escolha)]}')
 
 
    print("Produtos disponíveis:")
    print('produtos de limpeza ')
    print(produto_limpeza)
 
    while True:
        escolha = input("Digite o código do produto que deseja adicionar ao carrinho. \n'0800' - para proxima sessão. \n'70' - exit \n----->")
        if escolha == '0800':
            break
        if escolha == '70':
            break
        else:
       
            carrinho.append(produto_limpeza[int(escolha)])
            carrinho_preco.append(preco_p_l[int(escolha)])
 
            print(f"{produto_limpeza[int(escolha)]} adicionado ao carrinho.")
            print(f'{preco_p_l[int(escolha)]}')
 
    print("Produtos disponíveis:")
    print('produtos de higiene')
    print(produto_higiene)
 
    while True:
        escolha = input("Digite o código do produto que deseja adicionar ao carrinho. \n'0800' - para proxima sessão. \n'70' - exit \n----->")
        if escolha == '0800':
            break
        if escolha == '70':
            break
        else:
       
            carrinho.append(produto_higiene[int(escolha)])
            carrinho_preco.append(preco_p_h[int(escolha)])
            print(f"{produto_higiene[int(escolha)]} adicionado ao carrinho.")
            print(f'{preco_p_h[int(escolha)]}')
 
    for produto in carrinho_preco:
        total += float(produto)
   
    print(f"Total da compra: R$ {total}")
   
    forma_pagamento = input("Digite 'dinheiro' ou 'cartao': ")
   
    if forma_pagamento == 'dinheiro':
        valor_pago = float(input("Informe o valor pago: "))
        if valor_pago < total:
            print("Valor insuficiente. Pagamento não autorizado.")
        elif valor_pago > total:
            troco = valor_pago - total
            print(f"Troco: R$ {troco}")
            print("Compra autorizada. Obrigado!")
        else:
            print("Pagamento exato. Compra autorizada. Obrigado!")
    elif forma_pagamento == 'cartao':
        tipo_cartao = input("Digite 'debito', 'credito' ou 'vale': ")
        if tipo_cartao == 'debito' or tipo_cartao == 'credito' or tipo_cartao == 'vale':
            print("Compra autorizada. Obrigado!")
        else:
            print("Tipo de cartão inválido. Pagamento inválido.")
    else:
        print("Forma de pagamento inválida. Pagamento inválido.")