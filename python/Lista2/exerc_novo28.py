calculadora = int(input('Digite um numero de 1 a 4 '))
while calculadora<1 or calculadora>4:
    calculadora = int(input('Digite um numero de 1 a 4 '))
n1 = int(input('Digite um numero da operação que deseja realizar'))
n2 = int(input('Digite um numero da operação que deseja realizar '))
resultado = 0
if calculadora == 1:
    resultado = n1 + n2
elif calculadora == 2:
    if n1 < n2 :
        resultado = n2 - n1
    else:
        resultado = n1 - n2
elif calculadora == 3:
    resultado = n1 * n2
elif calculadora == 4:
    
    if n2 == 0:
        print('Numero invalido')
        quit()
    resultado = n1 / n2
       

print(f'O resultado é {resultado} ')
    

    

    
