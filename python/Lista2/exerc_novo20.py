n1 = int(input('Digite a nota n1 de 0 a 100: '))
n2 = int(input('Digite a nota n2 de 0 a 100: '))
n3 = int(input('Digite a nota n3 de 0 a 100: '))

nota = (n1 + n2 + n3 * 2)/4

print(nota)
if nota >= 60:
    print('Aprovado')
else:
    print('Reprovado')