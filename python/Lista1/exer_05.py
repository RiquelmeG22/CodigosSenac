cores = { 'azul':20, 'laranja' :30, 'roxo':40, 'preto' :50,}
cd = input('Digite azul laranja roxo  preto ')
try :
    cores.get(cd)
    print(f'O valor de {cd} é:{cores[cd]}')
except KeyError:
    print('Cor inexistente')    