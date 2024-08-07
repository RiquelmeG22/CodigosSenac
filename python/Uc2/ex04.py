
#Programe um software que recebe três números e cria duas funções: uma que retorna o
#maior número e outra que retorna o menor número.


def menor(a, b, c):
    return min(a, b, c)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))


print(f'O menor numero é {menor(n1, n2, n3)}')


def maior(a, b, c):
    return max(a, b, c)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))


print(f'O maior numero é {maior(n1, n2, n3)}')





