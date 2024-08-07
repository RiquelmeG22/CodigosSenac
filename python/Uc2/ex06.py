#Crie um software que recebe um número do usuário, passa esse valor para uma função e ela
#retorna o número escrito ao inverso. Por exemplo, se o usuário der o valor 1234, a função
#deve retornar 4321. Dica: primeiro, crie uma função que conta quantos dígitos tem um
#número.


def inverter(numero):
    return int(str(numero)[::-1])

numero = int(input('Digite um numero: '))
print(f'O numero invertido é {inverter(numero)}')