numeros = []
for i in range(15):
    numeros.append(int(input('Digite um numero inteiro')))
for i in range(15):
    if numeros[i] % 2 == 0:
        print(numeros[i])