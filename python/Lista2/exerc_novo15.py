nota1 = float(input('Digite sua nota '))
nota2 = float(input('Digite sua nota '))

if nota1 < 0.0 or nota1 > 10.0:
    print('A nota é invalida')
    quit()
elif nota2 < 0.0 or nota2 > 10.0:
    print('A nota 2 é invalida')
else:
        print(f'A media das nota {nota1} e {nota2} é = {(nota1 + nota2)/2:.2f}')        