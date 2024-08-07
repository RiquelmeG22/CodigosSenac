tabela_precos = {'azul': 20, 'laranja': 30, 'roxo': 40, 'preto': 50 }
while True:
    cor = input('Digite a cor do cd:')
    if cor.lower() == 'sair':
        break
    if int(cor) in tabela_precos:
        print(f'O preço do CD na cor {cor} é R${tabela_precos[cor.lower()]}')
    else:
        print('desculpe, essa cor nao esta na tabela de preço')


      