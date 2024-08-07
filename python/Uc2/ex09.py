#Escolha 0 para par ou 1 para ímpar. Em seguida, forneça um número. Crie um programa que
#determine se a soma do número escolhido com um número aleatório é par ou ímpar.


import random

escolha = int(input('Digite 0 para para ou 1 para ímpar: '))

numero = int(input('Digite um número '))

numaleatorio = random.randint(1,100)

soma = numero + numaleatorio

if soma % 2 == 0:
    print(f'A soma de {numero} com número {numaleatorio} é par. ')
else:
    print(f'A soma de {numero} com número {numaleatorio} é ímpar. ')
