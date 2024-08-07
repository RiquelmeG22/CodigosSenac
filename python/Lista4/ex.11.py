n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))
soma = 0
 
if n1 < n2:
        for i in range(n1 + 1, n2):
            soma  += i 
            print(i, end=' ')
            
else:
        for i in range(n2 + 1, n1):
            soma += i
            print(i, end=' ')
print(f'A soma dos valores é {soma}')            



