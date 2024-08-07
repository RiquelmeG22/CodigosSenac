salario = float(input('Informe seu sálario '))
taxa = 0 

if salario <= 2000:
    print('Isento')
else:
    if (salario <= 3000):
        taxa = (salario - 2000) * 0.08
    elif (salario <= 4500):
        taxa = 80 + (salario - 3000) * 0.18
    else:
        taxa = 80 + 270 + (salario - 4500) * 0.28
    print(f'O valor é {taxa:.2f}')
