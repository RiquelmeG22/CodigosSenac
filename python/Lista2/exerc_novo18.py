altura = float(input('Digite sua altura '))
sexo = input('Digite seu Sexo ')

if sexo.upper() == 'M':
    peso = (72.7 * altura) - 58
    print(f'O peso ideal é {peso}')
elif sexo.upper() == 'F':
    peso = (62.1 * altura) - 44.7
    print(f'O peso ideal é {peso}')
else :
    print('Sexo invalido.')  









