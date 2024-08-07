soma = 0
num = float(input('Digite um inteiro: '))
while num > 0:
    soma += num
    num -= 1
print(f'A soma dos numeros digitados é de {soma:,.2f}' )