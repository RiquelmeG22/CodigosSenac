gordin = 0.
indexG = -1
magrin = 999999.
indexM = -1
altin = 0.
indexA = -1
baixin = 999999.
indexB = -1

mass = []
height = []
code = []
index  = 0

def printUser(ind: int) -> str:
    return 'Usuário Código: {}, Altura: {}, Massa: {}'.format(code[ind], height[ind], mass[ind])

while True:
    code.append( int( input('Digite o código do usuário: ') ) )
    if(code[index] == 0):
        break

    mass.append( float( input('Digite a massa do usuário: ') ) )

    if(mass[index] > gordin):
        gordin = mass[index]
        indexG = index
    elif(mass[index] < magrin):
        magrin = mass[index]
        indexM = index

    height.append(float( input('Digite a altura do usuário: ') ) )
    if(height[index] > altin):
        altin = height[index]
        indexA = index
    elif(height[index] < baixin):
        baixin = height[index]
        indexB = index
    index += 1

print(f'Mais alto: {printUser(indexA)}')
print(f'Mais baixo: {printUser(indexB)}')
print(f'Mais gordo: {printUser(indexG)}')
print(f'Mais magro: {printUser(indexM)}')

print(f'Média massa: {sum(mass)/(len(mass)):.2f}')
print(f'Média altura: {sum(height)/(len(height)):.2f}')