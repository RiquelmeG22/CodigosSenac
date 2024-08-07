a = int(input('Digite A:'))
b = int(input('Digite B:'))
c = int(input('Digite C:'))

delta = b * b - (4 * a * c)

if(delta < 0):
    print('Não existe raiz')
elif(delta == 0):
    print('Raiz única')
else:
    print(f'Raiz X1: {(-b + delta ** 0.5) / (2 * a)}, X2: {(-b - delta ** 0.5) / (2 * a)}')