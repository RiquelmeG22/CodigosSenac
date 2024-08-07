
#Escreva uma função que recebe um número inteiro e retorna a soma de seus dígitos. Por 
#exemplo, se o número for 123, a função deve retornar 6 (1 + 2 + 3).

def soma(numero):
    soma = 0 
    while numero:
        soma += numero % 10
        numero //= 10
    return soma 


numero = int(input('Digite um numero '))
print(f'{soma(numero)}')