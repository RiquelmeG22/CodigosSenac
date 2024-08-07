
num = int(input('Digite um número para o mes '))
messes = ''

if num == 1:
    messes = 'Janeiro'
elif num == 2:
    messes = 'Fevereiro'
elif num == 3:
    messes = 'Março'
elif num == 4:
    messes = 'Abril'
elif num == 5:
    messes = 'Maio' 
elif num == 6:
    messes = 'Junho' 
elif num == 7:
    messes = 'Julho'                           
elif num == 8:
    messes = 'Agosto' 
elif num == 9:
    messes = 'Setembro' 
elif num == 10:
    messes = 'Outubro' 
elif num == 11:
    messes = 'Novembro' 
elif num == 12:
    messes = 'Dezembro'


if messes == '':
    print('Mes invalido ')
else:
    print(f'O mes correspondente é {messes}')    
