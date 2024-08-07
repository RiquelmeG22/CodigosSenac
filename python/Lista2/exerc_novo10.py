n = int(input('Digite um número '))
import math
tela = True

while tela == True:
    num1 = int(input('Digite um numero: '))

    if num1 > 0:
        quadrado = num1 * num1
        raiz = math.sqrt(num1)
        print(f'O numero digitado ao quadrado é: {quadrado}')
        print(f'A raiz do numero digitado é: {raiz}')
        tela = False
    elif num1 <= 0:
        print("numero invalido!")
        Tela = True
