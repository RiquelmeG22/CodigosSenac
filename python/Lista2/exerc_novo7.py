preco = float(input('Digite o preço da aquisição do produto '))
if preco < 50.0:
    print(f'Valor da venda é {preco * 1.45:.2f} ')
else:
    print(f'Valor da venda é {preco} ')    
