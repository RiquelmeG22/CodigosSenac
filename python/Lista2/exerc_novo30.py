state = {'MG':0.07, 'SP':0.12, 'RJ':0.15, 'MS':0.08}
price = float(input('Digite o preço do produto: '))

userState = input('Digite o estado em que vai vender:(MG, SP, RJ, MS) ')

if(userState.upper() in state):
    print(f'Preço no produto no estado {userState} é: {price * (1 + state[userState.upper()]):.2f}')
else:
    print('Estado digitado inválido!')