numero = int(input('Digite um valor'))
print(f'A tabuada do valor digitado é {numero}')
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')