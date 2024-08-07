semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
dia = int(input('Digite um numero para o dia da semana '))
dias = ''
if dia == 1:
    dias = 'Domingo'
    print(dias)
elif dia == 2:
    dias = 'Segunda'
elif dia == 3:
    dias = 'Terça'
elif dia == 4:
    dias = 'Quarta'        
elif dia == 5:
    dias = 'Quinta'
elif dia == 6:
    dias = 'Sexta'
elif dia == 7:
    dias = 'Sabado' 

if dias == '':
    print('Valor inválido') 
else:
    print(f'o dia correspondende é valor {dias}')


           



       

   